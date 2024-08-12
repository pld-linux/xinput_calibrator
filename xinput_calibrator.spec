#
# Conditional build:
%bcond_without	gtk	# GTK 2.x GUI (instead of native X11)

Summary:	A generic touchscreen calibration program for X.Org
Summary(pl.UTF-8):	Ogólny program do kalibracji ekranów dotykowych dla X.Org
Name:		xinput_calibrator
Version:	0.8.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
# Source0-md5:	ffeaf476092b2accd8cbdcba7bcab543
URL:		https://www.freedesktop.org/wiki/Software/xinput_calibrator/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
#BuildRequires:	desktop-file-utils
%{?with_gtk:BuildRequires:	gtkmm-devel >= 2.4}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.2
%{!?with_gtk:BuildRequires:	xorg-lib-libXrandr-devel}
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-inputproto-devel >= 1.5
BuildRequires:	xz
Requires:	xorg-lib-libXi >= 1.2
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
	--with-gui=%{?with_gtk:gtkmm}%{!?with_gtk:x11}

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

# Install xinput_calibrator.desktop :
#desktop-file-install \
#	--dir=$RPM_BUILD_ROOT%{_desktopdir} \
#	./scripts/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changelog README.md
%attr(755,root,root) %{_bindir}/xinput_calibrator
%{_mandir}/man1/xinput_calibrator.1*
%{_desktopdir}/xinput_calibrator.desktop
%{_pixmapsdir}/xinput_calibrator.svg
%{_pixmapsdir}/xinput_calibrator.xpm
