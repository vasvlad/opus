%define keepstatic 1
Name:     opus
Summary:  An audio codec for use in low-delay speech and audio communication
Version:  1.5.1
Release:  1
License:  BSD
URL:      https://www.opus-codec.org/
Source:   %{name}-%{version}.tar.gz

%description
Opus is a codec for interactive speech and audio transmission over the Internet.
Opus can handle a wide range of interactive audio applications, including
Voice over IP, videoconferencing, in-game  chat, and even remote live music
performances. It can scale from low bit-rate narrowband speech to very high
quality stereo music.
Opus, when coupled with an appropriate container format, is also suitable
for non-realtime  stored-file applications such as music distribution, game
soundtracks, portable music players, jukeboxes, and other applications that
have historically used high latency formats such as MP3, AAC, or Vorbis.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications that use %{name}.

%package devel-static
Summary:  Development files for %{name}

%description devel-static
This package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
OPUS_VERSION=$(echo %{version} | cut -d + -f 1)
cat > "package_version" <<EOF
AUTO_UPDATE=no
PACKAGE_VERSION="$OPUS_VERSION"
EOF

%reconfigure \
    --enable-shared \
    --enable-static \
    --enable-fixed-point \
    --enable-custom-modes \
    --disable-doc

%make_build

%install
%make_install

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libopus.so.*

%files devel-static
%defattr(-,root,root)
%{_libdir}/*a

%files devel
%defattr(-,root,root)
%doc README
%{_includedir}/opus
%{_libdir}/libopus.so
%{_libdir}/pkgconfig/opus.pc
%{_datadir}/aclocal/opus.m4
