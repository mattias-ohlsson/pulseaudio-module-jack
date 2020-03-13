Name:           pulseaudio-module-jack
Summary:        JACK support for the PulseAudio sound server
Version:        11.1
Release:        1%{?dist}
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/PulseAudio
Source:         https://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz

BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  automake libtool
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  m4
BuildRequires:  libtool-ltdl-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  libsndfile-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  avahi-devel
BuildRequires:  libatomic_ops-devel
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXi-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libICE-devel
BuildRequires:  xcb-util-devel
BuildRequires:  openssl-devel
BuildRequires:  orc-devel
BuildRequires:  libtdb-devel
BuildRequires:  pkgconfig(speexdsp) >= 1.2
BuildRequires:  libasyncns-devel
BuildRequires:  dbus-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(fftw3f)

Requires:       pulseaudio = %{version}
Requires:       jack-audio-connection-kit

%description
JACK sink and source modules for the PulseAudio sound server.

%prep
%autosetup -n pulseaudio-%{version}

%build
%configure \
  --enable-jack \
  --disable-option-checking \
  --disable-silent-rules \
  --disable-dependency-tracking \
  --disable-nls \
  --disable-rpath \
  --disable-atomic-arm-linux-helpers \
  --disable-libtool-lock \
  --disable-largefile \
  --disable-memfd \
  --disable-x11 \
  --disable-tests \
  --disable-oss-output \
  --disable-oss-wrapper \
  --disable-coreaudio-output \
  --disable-alsa \
  --disable-esound \
  --disable-solaris \
  --disable-waveout \
  --disable-glib2 \
  --disable-gtk3 \
  --disable-gconf \
  --disable-avahi \
  --disable-asyncns \
  --disable-tcpwrap \
  --disable-lirc \
  --disable-bluez4 \
  --disable-bluez5 \
  --disable-bluez5-ofono-headset \
  --disable-bluez5-native-headset \
  --disable-hal-compat \
  --disable-ipv6 \
  --disable-openssl \
  --disable-systemd-daemon \
  --disable-systemd-login \
  --disable-systemd-journal \
  --disable-manpages \
  --disable-per-user-esound-socket \
  --disable-default-build-tests \
  --disable-legacy-database-entry-format \
  --without-libiconv-prefix \
  --without-libintl-prefix \
  --without-caps \
  --without-fftw \
  --without-soxr

%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}/%{_libdir}/pulse-%{version}/modules
install -m 755 src/.libs/module-jack*.so %{buildroot}/%{_libdir}/pulse-%{version}/modules/

%files
%doc README
%license LICENSE GPL LGPL
%{_libdir}/pulse-%{version}/modules/module-jackdbus-detect.so
%{_libdir}/pulse-%{version}/modules/module-jack-sink.so
%{_libdir}/pulse-%{version}/modules/module-jack-source.so

%changelog
* Wed Mar 11 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 11.1-1
- Initial build
