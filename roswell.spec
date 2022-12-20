%undefine _debugsource_packages

Summary: Common Lisp environment setup Utility
Name: roswell
Version: 22.12.14.113
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
URL: https://github.com/roswell/roswell
BuildRequires: gcc
BuildRequires: automake
BuildRequires: libcurl-devel
BuildRequires: zlib-devel
Requires: make

%description
Roswell is a Lisp implementation installer/manager, launcher, and much more! It started as a command-line tool with the aim to make installing and managing Common Lisp implementations really simple and easy.

%prep
%setup -q
sh bootstrap

%build
%configure
%make_build

%install
%make_install PREFIX=%{_usr} LIBDIR=%{_libdir}

%files 

%{_sysconfdir}/%{name}
%{_bindir}/ros
%{_mandir}/man1/ros*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Dec 20 2022 makefunny <makefunny@outlook.com> - 22.12.14.113
- First build
