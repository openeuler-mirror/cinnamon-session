%global cinnamon_desktop_version 5.2.0

Name:    cinnamon-session
Version: 5.2.0
Release: 1
Summary: Cinnamon session manager
License: GPLv2+ and LGPLv2+
URL:     https://github.com/linuxmint/%{name}
Source0: https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-3.0) >= 2.99.0
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libnotify) >= 0.7.0
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
# this is so the configure checks find /usr/bin/halt etc.
BuildRequires: usermode
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(xapp) >= 1.4.6
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: meson
BuildRequires: intltool
BuildRequires: xmlto
BuildRequires: iptables-libs


Requires: system-logos
# Needed for cinnamon-settings-daemon
Requires: cinnamon-control-center-filesystem

# pull in dbus-x11, see bug 209924
Requires: dbus-x11

# we need an authentication agent in the fallback session
Requires: polkit-gnome
# an artificial requires to make sure we get dconf, for now
Requires: dconf

Requires: cinnamon-desktop >= %{cinnamon_desktop_version}

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
%autosetup -p1

%build
%meson \
 -Dgconf=false
%meson_build

%install
%meson_install
%ldconfig_scriptlets

%files
%doc AUTHORS README
%doc %{_mandir}/man*/*
%license COPYING
%{_bindir}/*
%{_libexecdir}/cinnamon-session-check-accelerated
%{_libexecdir}/cinnamon-session-check-accelerated-helper
%{_datadir}/cinnamon-session/
%{_datadir}/doc/cinnamon-session/dbus/cinnamon-session.html
%{_datadir}/icons/hicolor/*/apps/cinnamon-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/cinnamon-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.0-1
- Initial Packaging
