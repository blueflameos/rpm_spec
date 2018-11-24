Name:           firewatch-2016-game-wallpaper
Version:        1.0
Release:        1%{?dist}
Summary:        Firewatch 2016 Game Wallpaper
BuildArch:      noarch
License:        Unknown
URL:            http://www.firewatchgame.com
Source0:        firewatch_2016_game_wallpaper.jpg
  

%description
Firewatch 2016 Game Wallpaper.

%prep



%build



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/wallpapers/blueflameos
install -p -m 755 %{SOURCE0} %{buildroot}%{_datadir}/wallpapers/blueflameos

%files
%{_datadir}/wallpapers/blueflameos/firewatch_2016_game_wallpaper.jpg



%changelog
* Thu Nov 22 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-1
- Initial
