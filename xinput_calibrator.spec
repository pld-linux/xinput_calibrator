Summary:	A generic touchscreen calibration program for X.Org
Name:		xinput_calibrator
Version:	0.7.5
Release:	1
License:	MIT
Group:		X11/Applications
URL:		http://www.freedesktop.org/wiki/Software/xinput_calibrator
Source0:	https://github.com/tias/xinput_calibrator/archive/v%{version}.tar.gz
# Source0-md5:	b9fcb2c175a73e3c86af7688073de338
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel

%description
xinput_calibrator is a program for calibrating your touchscreen, when
using the X Window System. It currently features:
 - works for any standard Xorg touchscreen driver (uses XInput
   protocol)
 - mis-click detection (prevents bogus calibration)
 - dynamically recalibrates the evdev driver
 - outputs the calibration as xorg.conf.d snippet or HAL policy file
 - and more

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gui=gtkmm \
	--with-gui=x11

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

# Install xinput_calibrator.desktop :
desktop-file-install                       \
--dir=$RPM_BUILD_ROOT%{_desktopdir} \
./scripts/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.svg
%{_pixmapsdir}/%{name}.xpm
