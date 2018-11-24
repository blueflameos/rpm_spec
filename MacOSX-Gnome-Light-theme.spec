Name:           MacOSX-Gnome-Light-theme
Version:        1.0
Release:        1%{?dist}
Summary:        MacOSX Gnome Light Theme
BuildArch:      noarch
License:        Unknown
URL:            https://github.com/unc926/MacOSX_Gnome
Source0:        https://github.com/unc926/MacOSX_Gnome/archive/master.zip
  

%description
Gnome Shell Theme.

%prep
%autosetup -n MacOSX_Gnome-master

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes/
cp -r CF_Light %{buildroot}%{_datadir}/themes

%files
%doc README.md 
%{_datadir}/themes/CF_Light



%changelog
* Thu Nov 22 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-1
- Initial
