Summary: garp (gratuitous ARP)
Name: garp
Version: 0.1.1
Release: 1%{?dist}
URL: http://www.linuxvirtualserver.org/~acassen/
License: BSD
Group:  Applications/System
BuildRequires: gcc
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
garp (gratuitous ARP)

%prep
%setup
%{__perl} -pi.orig -e 's|/usr/local|/usr|g;' Makefile

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
%{makeinstall}

%clean

%files
%defattr(-, root, root)
/usr/bin/garp

