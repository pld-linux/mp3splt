Summary:	Tool for spliting MP3, Ogg files to tracks
Summary(pl):	Program do podzia³u plików MP3, Ogg na ¶cie¿ki
Name:		mp3splt
Version:	2.1c
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mp3splt/%{name}-%{version}-src.tar.gz
# Source0-md5:	b355835e4d57b8b921a14a6485244c87
Patch0:		%{name}-gcc4.patch
URL:		http://mp3splt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
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

%description -l pl
Mp3Splt jest narzêdziem do podzia³u plików MP3 i Ogg na ¶cie¿ki.
Dzia³a bez potrzeby dekodowania pliku. Jest bardzo przydatny do
podzia³u du¿ych plików MP3/Ogg na mniejsze pliki lub do podzia³u
ca³ego albumu w celu uzyskania poszczególnych ¶cie¿ek. W tym drugim
przypadku mo¿liwe jest ustalenie momentów zmiany plików oraz rêczne
b±d¼ automatyczne (pobierane z CDDB lub plików .cue) ustalanie nazw
plików.

Je¶li posiadasz plik stworzony za pomoc± Mp3Wrap lub AlbumWrap, mo¿esz
wydobyæ poszczególne ¶cie¿ki w przeci±gu zaledwie kilku sekund.
Program obs³uguje MP3 z VBR.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
