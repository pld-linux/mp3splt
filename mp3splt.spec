Summary:	Tool for spliting mp3,ogg files to tracks
Summary(pl):	Program do podzia³u plików mp3,ogg na ¶cie¿ki
Name:		mp3splt
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://flow.dl.sourceforge.net/sourceforge/mp3splt/%{name}-%{version}-src.tar.gz
# Source0-md5:	c3830bc7f98d344ad371a5e1a7acc91e
URL:		mp3splt.sourceforge.net
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
Requires:	libogg
Requires:	libvorbis
Requires:	mad
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mp3Splt is a command line utility to split mp3 and ogg files selecting 
a begin and an end time position, without decoding. It's very useful to 
split large mp3/ogg to make smaller files or to split entire albums to 
obtain original tracks. If you want to split an album, you can select split
points and filenamesmanually or you can get them automatically from CDDB 
(internet or a local file) or from .cue files.
Otherwise if you have a file created either with Mp3Wrap or AlbumWrap you 
can extract tracks just in few seconds. Supports VBR mp3.
%description -l pl
Mp3Splt jest narzêdziem do podzia³u plików mp3 i ogg na ¶cie¿ki. Dzia³a
bez potrzeby dekodowania pliku. Obs³uguje pliki cue oraz pobieranie danych
z CDDB. Wspiera pliki mp3 zakodowane z VBR.

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README ABOUT-NLS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1
