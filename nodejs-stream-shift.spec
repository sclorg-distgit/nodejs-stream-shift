%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name stream-shift

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        4%{?dist}
Summary:        Returns the next buffer/object in a stream's readable queue

License:        MIT
URL:            https://github.com/mafintosh/stream-shift
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
BuildRequires:  %{?scl_prefix}npm(through2)
%endif

%description
%{summary}.

%prep
%autosetup -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
tape test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-4
- rh-nodejs8 rebuild

* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Missing macro

* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Convert to scl

* Sat Sep 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
