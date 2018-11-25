%global uuid simplenetspeed@biji.extension
%global fname simplenetspeed-master
Name:           gnome-shell-extension-simple-net-speed
Version:        5
Release:        2%{?dist}
Summary:        Simple net speed
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/biji/simplenetspeed
Source0:        https://github.com/biji/simplenetspeed/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Gnome extension to show network speed.

%prep
%setup -q -n %{fname}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.simplenetspeed.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.simplenetspeed.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.simplenetspeed.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Wed May 02 2018 yucefsourani <youssef.m.sourani@gmail.com> - 5-2
- Release 2

* Sun Jul 09 2017 youcef sourani <youssef.m.sourani@gmail.com> - 5-1.
- Initial For f26
