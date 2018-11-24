Name:           McOS-MJV-3.30-theme
Version:        1.0
Release:        2%{?dist}
Summary:        McOS-MJV-3.30-theme Theme
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/paullinuxthemer/Mc-OS-themes
Source0:        https://github.com/paullinuxthemer/Mc-OS-themes/archive/master.zip
  

%description
Gtk Theme.

%prep
%autosetup -n Mc-OS-themes-master

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes/
cp -r McOS-MJV-3.30 %{buildroot}%{_datadir}/themes

%files
%license COPYING 
%doc README.md 
%{_datadir}/themes/McOS-MJV-3.30



%changelog
* Thu Nov 22 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-2
- Release 2

* Thu Nov 22 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-1
- Initial
