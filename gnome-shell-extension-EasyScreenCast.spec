%global uuid EasyScreenCast@iacopodeenosee.gmail.com
Name:           gnome-shell-extension-EasyScreenCast
Version:        0.10
Release:        2%{?dist}
Summary:        EasyScreenCast GNOME Shell Extension
BuildArch:      noarch
License:        GPLv3
URL:            https://iacopodeenosee.wordpress.com/
Source0:        https://github.com/EasyScreenCast/EasyScreenCast/archive/%{version}.tar.gz
BuildRequires:  gettext
Requires(post): pkgconfig(glib-2.0)

%description
EasyScreenCast simplifies the use of the video recording function integrated in gnome shell, allows quickly to change the various settings of the desktop recording.

%prep
%setup -q -n EasyScreenCast-%{version}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -m 0644 schemas/org.gnome.shell.extensions.easyscreencast.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.easyscreencast.gschema.xml

%find_lang EasyScreenCast@iacopodeenosee.gmail.com

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%files -f EasyScreenCast@iacopodeenosee.gmail.com.lang
%{_datadir}/gnome-shell/extensions/%{uuid}/*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.easyscreencast.gschema.xml

%changelog
* Wed May 02 2018 yucefsourani <youssef.m.sourani@gmail.com> - 0.10-2
- Release 2

* Fri Nov 17 2017 yucef sourani <youssef.m.sourani@gmail.com> - 0.10-1
- Initial for fedora 27

