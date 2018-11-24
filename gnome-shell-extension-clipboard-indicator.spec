%global uuid clipboard-indicator@tudmotu.com
Name:           gnome-shell-extension-clipboard-indicator
Version:        30
Release:        2%{?dist}
Summary:        Clipboard Indicator GNOME Shell Extension
BuildArch:      noarch
License:        MIT
URL:            https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator
Source0:        https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator/archive/v%{version}.tar.gz
#Patch0: gnome-shell-extension-clipboard-indicator_disable_notify_on_copy.patch
BuildRequires:  gettext
#BuildRequires:  patch
Requires(post): pkgconfig(glib-2.0)

%description
Clipboard Manager extension for Gnome-Shell - Adds a clipboard indicator to the top panel, and caches clipboard history.

%prep
%setup -q 
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 schemas/org.gnome.shell.extensions.clipboard-indicator.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.clipboard-indicator.gschema.xml
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%find_lang clipboard-indicator

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ &>/dev/null || :


%files  -f clipboard-indicator.lang
%{_datadir}/gnome-shell/extensions/%{uuid}/*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.clipboard-indicator.gschema.xml

%changelog
* Wed May 02 2018 yucefsourani <youssef.m.sourani@gmail.com> - 30-2
- Release 2

* Sun Apr 08 2018 youcef sourani <youssef.m.sourani@gmail.com> - 30-1
- Update To v30

* Fri Nov 17 2017 yucef sourani <youssef.m.sourani@gmail.com> - 29-1
- Initial for fedora 27

