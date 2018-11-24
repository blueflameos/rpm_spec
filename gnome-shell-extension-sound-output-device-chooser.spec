%global uuid sound-output-device-chooser@kgshank.net
%global fname gse-sound-output-device-chooser-master
Name:           gnome-shell-extension-sound-output-device-chooser
Version:        17.0
Release:        1%{?dist}
Summary:        Shows a list of sound output and input devices
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/kgshank/gse-sound-output-device-chooser
Source0:        https://github.com/kgshank/gse-sound-output-device-chooser/archive/master.zip
Requires(post): pkgconfig(glib-2.0)


%description
Shows a list of sound output and input devices (similar to gnome sound settings) 
in the status menu below the volume slider. Various active ports like HDMI , 
Speakers etc. of the same device are also displayed for selection

%prep
%setup -q -n %{fname}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{uuid}/schemas/org.gnome.shell.extensions.sound-output-device-chooser.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.sound-output-device-chooser.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r %{uuid}/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%files
%doc README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.sound-output-device-chooser.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/*

%changelog
* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 17.0-1
- Initial
