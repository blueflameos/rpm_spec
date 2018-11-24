Name:           la-capitaine-icon-theme
Version:        0.6.1
Release:        1%{?dist}
Summary:        la-capitaine-icon-theme Icons Theme
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/keeferrourke/la-capitaine-icon-theme
Source0:        https://github.com/keeferrourke/la-capitaine-icon-theme/archive/v%{version}.tar.gz
  

%description
la-capitaine-icon-theme Icons Theme.

%prep
%autosetup

%build
yes | ./configure 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/icons/la-capitaine-icon-theme
cp -r * %{buildroot}%{_datadir}/icons/la-capitaine-icon-theme

%files
%license LICENSE COPYING
%doc Credits.md README.md Thanks.md
%{_datadir}/icons/la-capitaine-icon-theme



%changelog
* Thu Nov 22 2018 yucefsourani <youssef.m.sourani@gmail.com> - 0.6.1-1
- Initial
