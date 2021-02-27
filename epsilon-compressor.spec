# NOTE: package name is epsilon, but:
# - it's somehow common name
# - it was already occupied by (obsolete now) epsilon library from Enlightenment project
# so let's use more specific package name.
# TODO: MPI support
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	EPSILON - powerful Open Source wavelet compressor
Summary(pl.UTF-8):	EPSILON - potężny kompresor falkowy o otwartych źródłach
Name:		epsilon-compressor
Version:	0.9.2
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/epsilon-project/epsilon-%{version}.tar.gz
# Source0-md5:	56d7f1a41e05be20441728d9e20d22ef
Source1:	http://downloads.sourceforge.net/epsilon-project/refman-%{version}.tar.gz
# Source1-md5:	953a9e86cfb7435db24ebe5c0c6b1837
Patch0:		epsilon-link.patch
URL:		http://sourceforge.net/projects/epsilon-project/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	popt-devel
Conflicts:	epsilon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EPSILON is a powerful OpenSource wavelet image compressor.
Wavelet-driven compressors are know to be much more effective than
traditional DCT-based ones (like JPEG). At the moment, the program
supports 30+ different wavelet filters, runs in parallel in
multi-threaded and MPI environments, can process HUGE images and much
more!

%description -l pl.UTF-8
EPSILON to potężny kompresor falkowy dla obrazów, mający otwarte
źródła. Kompresory falkowe są zwykle o wiele bardziej efektywne od
tradycyjnych, opartych na dyskretnej transformacie cosinusowej (DCT),
takich jak JPEG. Obecnie program obsługuje ponad 30 różnych filtrów
falkowych, działa równolegle w środowisku wielowątkowym oraz MPI i
potrafi przetwarzać OGROMNE obrazy.

%package devel
Summary:	Header files for EPSILON library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki EPSILON
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	epsilon-devel

%description devel
Header files for EPSILON library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki EPSILON.

%package static
Summary:	Static EPSILON library
Summary(pl.UTF-8):	Statyczna biblioteka EPSILON
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	epsilon-static

%description static
Static EPSILON library.

%description static -l pl.UTF-8
Statyczna biblioteka EPSILON.

%package apidocs
Summary:	EPSILON API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki EPSILON
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for EPSILON library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki EPSILON.

%prep
%setup -q -n epsilon-%{version} -a1
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-pthreads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README README.cluster README.mpich TODO
%attr(755,root,root) %{_bindir}/epsilon
%attr(755,root,root) %{_bindir}/start_epsilon_nodes.pl
%attr(755,root,root) %{_bindir}/stop_epsilon_nodes.pl
%attr(755,root,root) %{_libdir}/libepsilon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libepsilon.so.1
%{_mandir}/man1/epsilon.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepsilon.so
%{_libdir}/libepsilon.la
%{_includedir}/epsilon.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libepsilon.a

%files apidocs
%defattr(644,root,root,755)
%doc html/*
