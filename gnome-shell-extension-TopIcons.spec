%global uuid TopIcons@phocean.net
%global fname TopIcons-plus
Name:           gnome-shell-extension-TopIcons
Version:        22
Release:        1%{?dist}
Summary:        legacy tray icons
BuildArch:      noarch
License:        GPLv2
URL:            https://github.com/phocean/TopIcons-plus
Source0:        https://github.com/phocean/TopIcons-plus/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
This extension moves legacy tray icons (bottom left of Gnome Shell) to the top panel. 
It is a fork from the original extension from ag  with settings for icon opacity, 
saturation, padding, size and tray position, along with a few minor fixes and 
integration with the Skype integration extension.

%prep
%setup -q -n %{fname}-master

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.topicons.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.topicons.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license gpl-2.0.txt
%doc  README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.topicons.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Sat Nov 24 2018 yucefsourani <youssef.m.sourani@gmail.com> - 22-1
- Initial
