Summary:	Tool for spliting MP3, Ogg files to tracks
Summary(pl.UTF-8):	Program do podziału plików MP3, Ogg na ścieżki
Name:		mp3splt
Version:	2.3a
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/mp3splt/%{name}-%{version}.tar.gz
# Source0-md5:	1fe663f7de5a6949bbe5b6aa78fea79f
URL:		http://mp3splt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libmp3splt-devel >= 0.6.1a
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mp3Splt is a command line utility to split MP3 and Ogg files selecting
a begin and an end time position, without decoding. It's very useful
to split large MP3/Ogg to make smaller files or to split entire albums
to obtain original tracks. If you want to split an album, you can
select split points and filenames manually or you can get them
automatically from CDDB (internet or a local file) or from .cue files.

Otherwise if you have a file created either with Mp3Wrap or AlbumWrap
you can extract tracks just in few seconds. Supports VBR MP3.

%description -l pl.UTF-8
Mp3Splt jest narzędziem do podziału plików MP3 i Ogg na ścieżki.
Działa bez potrzeby dekodowania pliku. Jest bardzo przydatny do
podziału dużych plików MP3/Ogg na mniejsze pliki lub do podziału
całego albumu w celu uzyskania poszczególnych ścieżek. W tym drugim
przypadku możliwe jest ustalenie momentów zmiany plików oraz ręczne
bądź automatyczne (pobierane z CDDB lub plików .cue) ustalanie nazw
plików.

Jeśli posiadasz plik stworzony za pomocą Mp3Wrap lub AlbumWrap, możesz
wydobyć poszczególne ścieżki w przeciągu zaledwie kilku sekund.
Program obsługuje MP3 z VBR.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -Im4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-oggsplt_symlink
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mp3splt
%attr(755,root,root) %{_bindir}/oggsplt
%{_mandir}/man1/mp3splt.1*
%{_mandir}/man1/oggsplt.1*
