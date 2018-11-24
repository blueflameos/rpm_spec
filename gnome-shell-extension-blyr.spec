%global uuid  	blyr@yozoon.dev.gmail.com
%global fname gnome-shell-extension-blyr-master
Name:           gnome-shell-extension-blyr
Version:        5.0
Release:        1%{?dist}
Summary:        Apply a Blur Effect to GNOME Shell UI elements
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/yozoon/gnome-shell-extension-blyr
Source0:        https://github.com/yozoon/gnome-shell-extension-blyr/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Apply a Blur Effect to GNOME Shell UI elements.

%prep
%setup -q -n %{fname}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{uuid}/schemas/org.gnome.shell.extensions.blyr.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.blyr.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r %{uuid}/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%doc README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.blyr.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 5.0-1
- Initial
