Name: ansible-xml
BuildArch: noarch
Version: 0.3.1
Release: 1
Summary: Ansible module for manipulating bits and pieces of XML files and strings
Vendor: Chris Prescott
License: GPLv2
URL: https://github.com/cmprescott/ansible-xml
Packager: Styopa Semenukha <semenukha@gmail.com>

Requires: python-lxml >= 2.3
Source: https://github.com/cmprescott/%name/archive/%name-%version.tar.gz

%define ansible_lib %{_datarootdir}/ansible

%description
Ansible module for manipulating bits and pieces of XML files and strings

%prep
%setup

%install
%{__mkdir_p} %buildroot%{ansible_lib}
%{__install} -m 644 library/xml %buildroot%{ansible_lib}/xml

%files
%{ansible_lib}/xml

%clean
%{__rm} -rf %_buildrootdir
