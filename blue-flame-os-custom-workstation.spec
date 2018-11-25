Name:           blue-flame-os-custom-workstation
Version:        29
Release:        3%{?dist}
Summary:        Blue Flame OS Custom Gnome Shell Files
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/blueflameos/blue-flame-os-custom-workstation
Source0:        https://github.com/blueflameos/blue-flame-os-custom-workstation/archive/master.zip
Requires(post): pkgconfig(glib-2.0)       
Requires:       breeze-cursor-theme
Requires:       McOS-MJV-3.30-theme
Requires:       MacOSX-Gnome-Light-theme 
Requires:       firewatch-2016-game-wallpaper
Requires:       la-capitaine-icon-theme 

%description
Blue Flame OS Custom Gnome Shell Files.

%prep
%setup -q -n blue-flame-os-custom-workstation-master

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -r ./60_* %{buildroot}%{_datadir}/glib-2.0/schemas/

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license LICENSE
%{_datadir}/glib-2.0/schemas/*


%changelog
* Sun Nov 25 2018 yucefsourani <youssef.m.sourani@gmail.com> - 29-3
- Release 3

* Sun Nov 25 2018 yucefsourani <youssef.m.sourani@gmail.com> - 29-2
- Release 2

* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 29-1
- Initial
