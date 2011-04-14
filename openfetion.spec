Summary: IM client based on GTK+2.0, using CHINA MOBILE's Fetion Protocol Version 4
Name: openfetion
Version: 2.1.0
Release: %mkrel 2
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1: openfetion-1.7-str-fmt.patch
BuildRoot: %{_tmppath}/%{name}-root
Buildrequires: gtk2-devel
BuildRequires: libnotify-devel
BuildRequires: libgstreamer-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: libofetion-devel >= %{version}
BuildRequires: cmake

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -qn %name-%version

%build
%cmake -DWITH_NETWORKMANAGER=OFF
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
