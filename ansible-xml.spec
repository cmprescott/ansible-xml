Name: ansible-xml
BuildArch: noarch
Version: 1.0.0
Release: 1
Summary: Ansible module for manipulating bits and pieces of XML files and strings
Vendor: Chris Prescott
License: GPLv3
URL: https://github.com/cmprescott/ansible-xml
Packager: Styopa Semenukha <semenukha@gmail.com>

Requires: python-lxml >= 2.3
Source: https://github.com/cmprescott/%name/archive/%version.tar.gz

%bcond_with docs

%if %{with docs}
BuildRequires: markdown
%endif

%define ansible_lib %{_datarootdir}/ansible

%description
Ansible module for manipulating bits and pieces of XML files and strings

%prep
%setup

%build
%if %{with docs}
markdown CHANGELOG.md > CHANGELOG.html
markdown README.md > README.html
%endif

%install
%{__mkdir_p} %buildroot%{ansible_lib}
%{__install} -m 644 library/xml %buildroot%{ansible_lib}/xml

%files
%{ansible_lib}/xml
%if %{with docs}
%doc CHANGELOG.html README.html
%endif

%clean
%{__rm} -rf %_buildrootdir
