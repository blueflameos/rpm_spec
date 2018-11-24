%global uuid dash-to-dock@micxgx.gmail.com
Name:           gnome-shell-extension-dash-to-dock
Version:        64
Release:        1%{?dist}
Summary:        A dock for the GNOME Shell
License:        GPLv2+
URL:            https://github.com/micheleg/dash-to-dock
Source0:        https://github.com/micheleg/dash-to-dock/archive/extensions.gnome.org-v%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  vala-tools
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
Requires(post): pkgconfig(glib-2.0)


%description
A dock for the Gnome Shell. This extension moves the dash out of the overview
transforming it in a dock for an easier launching of applications and a faster
switching between windows and desktops.

%prep
%setup -q -n dash-to-dock-extensions.gnome.org-v%{version}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALLBASE=%{buildroot}%{_datadir}/gnome-shell/extensions/ VERSION=%{version}

mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml

%find_lang dashtodock

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files -f dashtodock.lang
%doc README.md COPYING
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 64-1
- Version 64

* Wed May 02 2018 yucefsourani <youssef.m.sourani@gmail.com> - 63-3
- Release 3

* Sun Apr 08 2018 youcef sourani <youssef.m.sourani@gmail.com> - 63-2
- Update To v63

* Fri Nov 17 2017 yucef sourani <youssef.m.sourani@gmail.com> - 61-1
- Initial for fedora 27

