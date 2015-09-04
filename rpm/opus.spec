Name:          opus
Version:       1.1
Release:       0
Summary:       A codec for interactive speech and audio transmission over the Internet
Group:         Applications/Multimedia
URL:           http://www.opus-codec.org
Source:        http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
License:       BSD

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

%package       devel
Group:         Development/Libraries
Summary:       Development files for %{name}
Requires:      Requires: %{name} = %{version}-%{release}
Requires:      pkgconfig

%description   devel
This package contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build

OPUS_VERSION=$(echo %{version} | cut -d + -f 1)
cat > "package_version" <<EOF
AUTO_UPDATE=no
PACKAGE_VERSION="$OPUS_VERSION"
EOF

./autogen.sh
%configure \
    --enable-shared \
    --disable-static \
    --enable-fixed-point \
    --disable-float-api \
    --enable-custom-modes \
    --disable-doc

make %{?jobs:-j%jobs}

%check
make check

%install
%make_install

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libopus.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/opus/opus*.h
%{_libdir}/libopus.so
%{_libdir}/pkgconfig/opus.pc
%{_datadir}/aclocal/opus.m4
