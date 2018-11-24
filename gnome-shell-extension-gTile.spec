%global uuid gTile@vibou
%global fname  gTile
Name:           gnome-shell-extension-gTile
Version:        28
Release:        1%{?dist}
Summary:        Tile windows on a grid
BuildArch:      noarch
License:        GPLv2
URL:            https://github.com/gTile/gTile
Source0:        https://github.com/gTile/gTile/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Tile windows on a grid.

%prep
%setup -q -n %{fname}-master

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.gtile.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gtile.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license LICENSE
%doc  README.md CHANGELOG.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gtile.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Sat Nov 24 2018 yucefsourani <youssef.m.sourani@gmail.com> - 22-1
- Initial
