%global uuid netspeed@hedayaty.gmail.com
%global fname NetSpeed-master
Name:           gnome-shell-extension-netspeed
Version:        28
Release:        2%{?dist}
Summary:        Displays Internet Speed
BuildArch:      noarch
License:        GPLv2
URL:            https://github.com/hedayaty/NetSpeed
Source0:        https://github.com/hedayaty/NetSpeed/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Gnome Extension To Displays Internet Speed.

%prep
%setup -q -n %{fname}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.netspeed.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.netspeed.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license gpl-2.0.md
%doc  CHANGELOG
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.netspeed.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 28-2
- Release 2

* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 28-1
- Initial
