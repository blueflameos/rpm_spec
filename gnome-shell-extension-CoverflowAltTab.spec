%global uuid CoverflowAltTab@dmo60.de
Name:           gnome-shell-extension-CoverflowAltTab
Version:        1.5.1
Release:        1%{?dist}
Summary:        CoverflowAltTab GNOME Shell Extension
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/dmo60/CoverflowAltTab
Source0:        https://github.com/dmo60/CoverflowAltTab/archive/v%{version}.tar.gz
BuildRequires:  gettext
Requires(post): pkgconfig(glib-2.0)


%description
CoverflowAltTab is an Alt-Tab replacement available as an extension for Gnome-Shell and Cinnamon,
it let's you Alt-Tab through your windows in a cover-flow manner.

%prep
%setup -q -n CoverflowAltTab-%{version}
rm buildforupload.sh
rm -r img

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r %{uuid}/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -m 0644 CoverflowAltTab@dmo60.de/schemas/org.gnome.shell.extensions.coverflowalttab.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.coverflowalttab.gschema.xml

%find_lang coverflow

%files -f coverflow.lang
%doc README.markdown COPYING CONTRIBUTORS.markdown
%{_datadir}/gnome-shell/extensions/%{uuid}/*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.coverflowalttab.gschema.xml

%changelog
* Fri Nov 23 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.5.1-1
- Version 1.5.1

* Wed May 02 2018 yucefsourani <youssef.m.sourani@gmail.com> - 1.4.1-2
- Release 2

* Fri Nov 17 2017 yucef sourani <youssef.m.sourani@gmail.com> - 1.4.1-1
- Initial for fedora 27

