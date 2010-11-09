Summary: IM client based on GTK+2.0, using CHINA MOBILE's Fetion Protocol Version 4
Name: openfetion
Version: 2.0.1
Release: %mkrel 1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1: openfetion-1.7-str-fmt.patch
BuildRoot: %{_tmppath}/%{name}-root
Buildrequires: gtk2-devel
BuildRequires: openssl-devel
BuildRequires: libnotify-devel
BuildRequires: libxml2-devel
BuildRequires: libgstreamer-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: sqlite3-devel
BuildRequires: intltool

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -qn %name-%version

%build
%configure2_5x --disable-static --disable-nm
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%_includedir %buildroot%_libdir/*.{la,so} %buildroot%_libdir/pkgconfig/*.pc

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_libdir}/lib*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
