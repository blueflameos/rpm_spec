%global uuid unlockDialogBackground@sun.wxg@gmail.com
%global fname gnome-shell-extension-unlockDialogBackground-master
Name:           gnome-shell-extension-unlockDialogBackground
Version:        1.0
Release:        2%{?dist}
Summary:        Change unlock dialog background
BuildArch:      noarch
License:        MIT
URL:            https://github.com/sunwxg/gnome-shell-extension-unlockDialogBackground
Source0:        https://github.com/sunwxg/gnome-shell-extension-unlockDialogBackground/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Change unlock dialog background,
You can change background picture from extension settings.

%prep
%setup -q -n %{fname}
sed -i -- 's/\/path\/to\/picture/file:\/\/\/usr\/share\/wallpapers\/blueflameos\/firewatch_2016_game_wallpaper.jpg/g' %{uuid}/schemas/org.gnome.shell.extensions.unlockDialogBackground.gschema.xml

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{uuid}/schemas/org.gnome.shell.extensions.unlockDialogBackground.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.unlockDialogBackground.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r %{uuid}/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.unlockDialogBackground.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Sun Nov 25 2018 yucefsourani <youssef.m.sourani@gmail.com> - 2.0-2
- Release 2

* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 2.0-1
- Initial
