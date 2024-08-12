Summary:	A generic touchscreen calibration program for X.Org
Summary(pl.UTF-8):	Ogólny program do kalibracji ekranów dotykowych dla X.Org
Name:		xinput_calibrator
Version:	0.7.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://github.com/tias/xinput_calibrator/archive/v%{version}.tar.gz
# Source0-md5:	b9fcb2c175a73e3c86af7688073de338
URL:		http://www.freedesktop.org/wiki/Software/xinput_calibrator
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xinput_calibrator is a program for calibrating your touchscreen, when
using the X Window System. It currently features:
- works for any standard Xorg touchscreen driver (uses XInput
  protocol)
- mis-click detection (prevents bogus calibration)
- dynamically recalibrates the evdev driver
- outputs the calibration as xorg.conf.d snippet or HAL policy file
- and more

%description -l pl.UTF-8
xinput_calibrator to program do kalibrowania ekranów dotykowych na
potrzeby używania z X Window System. Aktualne możliwości to m.in:
- działanie z dowolnym sterownikiem ekranu dotykowego Xorg
  (wykorzystuje protokół XInput)
- wykrywanie niechcianych kliknięć (zapobiega błędnej kalibracji)
- dynamiczna rekalibracja sterownika evdev
- wyjście kalibracji w postaci fragmentu xorg.conf.d lub pliku
  polityki HAL

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
desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_desktopdir} \
	./scripts/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/xinput_calibrator
%{_mandir}/man1/xinput_calibrator.1*
%{_desktopdir}/xinput_calibrator.desktop
%{_pixmapsdir}/xinput_calibrator.svg
%{_pixmapsdir}/xinput_calibrator.xpm
