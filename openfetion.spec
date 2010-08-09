Summary: IM client based on GTK+2.0, using CHINA MOBILE's Fetion Protocol Version 4
Name: openfetion
Version: 1.7
Release: %mkrel 1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: openfetion-1.7-disable-ldconfig.patch
Patch1: openfetion-1.7-str-fmt.patch
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
%patch0 -p0 -b .ld
%patch1 -p0 -b .str

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%_includedir %buildroot%_libdir/*.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_libdir}/lib*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
