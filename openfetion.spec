Summary: IM client based on GTK+2.0, using CHINA MOBILE's Fetion Protocol Version 4
Name: openfetion
Version: 1.6.1
Release: %mkrel 1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: openfetion-1.6.1-link.patch
BuildRoot: %{_tmppath}/%{name}-root
Buildrequires: gtk2-devel
BuildRequires: openssl-devel
BuildRequires: libnotify-devel
BuildRequires: libxml2-devel
BuildRequires: libgstreamer-devel

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -qn %name-%version
%patch0 -p0 -b .link

%build
autoreconf -fi
%define Werror_cflags %nil
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
