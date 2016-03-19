%define major 1
%define oname verto
%define libverto %mklibname %{oname} %{major}
%define devverto %mklibname %{oname} -d
%define libglib %mklibname %{oname}-glib %{major}
%define devglib %mklibname %{oname}-glib -d
%define libev %mklibname %{oname}-libev %{major}
%define devev %mklibname %{oname}-libev -d
%define libevent %mklibname %{oname}-libevent %{major}
%define devevent %mklibname %{oname}-libevent -d
%define	libtevent %mklibname %{oname}-tevent %{major}
%define	devtevent %mklibname %{oname}-tevent -d

%bcond_with	crosscompile

Name:		libverto
Version:	0.2.5
Release:	13
Summary:	Main loop abstraction library
Group:		System/Libraries
License:	MIT
Url:		https://fedorahosted.org/libverto/
Source0:	http://fedorahosted.org/releases/l/i/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libev)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(tevent)

%description
libverto provides a way for libraries to expose asynchronous interfaces
without having to choose a particular event loop, offloading this
decision to the end application which consumes the library.

If you are packaging an application, not library, based on libverto,
you should depend either on a specific implementation module or you
can depend on the virtual provides 'libverto-module-base'. This will
ensure that you have at least one module installed that provides io,
timeout and signal functionality. Currently glib is the only module
that does not provide these three because it lacks signal. However,
glib will support signal in the future.

%package   -n	%{libverto}
Summary:	System libraries for %{name}
Group:		System/Libraries

%description -n %{libverto}
The %{name} package contains libraries for %{name}.

%package   -n	%{devverto}
Summary:	Development files for %{name}
Group:		Development/C 
Requires:	%{libverto} = %{version}-%{release}

%description -n %{devverto}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	%{libglib}
Summary:	glib module for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}glib < 0.2.5-1

%description -n %{libglib}
Module for %{name} which provides integration with glib.

This package does NOT yet provide %{name}-module-base.

%package  -n	%{devglib}
Summary:        Development files for %{name}-glib
Group:		Development/C 
Requires:       %{libglib} = %{version}-%{release}
Requires:       %{devverto} = %{version}-%{release}

%description -n %{devglib}
The %{name}-glib-devel package contains libraries and header files for
developing applications that use %{name}-glib.

%package -n     %{libev}
Summary:        libev module for %{name}
Group:		System/Libraries
Provides:       %{name}-module-base = %{version}-%{release}
Obsoletes:	%{_lib}ev < 0.2.5-1

%description -n %{libev}
Module for %{name} which provides integration with libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n    %{devev}
Summary:        Development files for %{name}-libev
Group:		Development/C 
Requires:       %{libev} = %{version}-%{release}
Requires:       %{devverto} = %{version}-%{release}

%description -n %{devev}
The %{name}-libev-devel package contains libraries and header files for
developing applications that use %{name}-libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n    %{libevent}
Summary:        libevent module for %{name}
Group:		System/Libraries
Provides:       %{name}-module-base = %{version}-%{release}
Obsoletes:	%{_lib}event < 0.2.5-1

%description -n %{libevent}
Module for %{name} which provides integration with libevent.

%package   -n   %{devevent}
Summary:        Development files for %{name}-libevent
Group:		Development/C 
Requires:       %{libevent} = %{version}-%{release}
Requires:       %{devverto} = %{version}-%{release}

%description -n %{devevent}
The %{name}-libevent-devel package contains libraries and header files for
developing applications that use %{name}-libevent.

%package   -n   %{libtevent}
Summary:        tevent module for %{name}
Group:		System/Libraries
Provides:       %{name}-module-base = %{version}-%{release}
Obsoletes:	%{_lib}tevent < 0.2.5-1

%description -n   %{libtevent}
Module for %{name} which provides integration with tevent.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n	%{devtevent}
Summary:        Development files for %{name}-tevent
Group:		Development/C 
Requires:       %{libtevent} = %{version}-%{release}
Requires:       %{devverto} = %{version}-%{release}

%description -n %{devtevent}
The %{name}-tevent-devel package contains libraries and header files for
developing applications that use %{name}-tevent.

%prep
%setup -q
%apply_patches

%build
autoreconf -fiv
%configure --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README

%files -n %{libverto}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devverto}
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libglib}
%{_libdir}/%{name}-glib.so.%{major}*

%files -n %{devglib}
%{_includedir}/verto-glib.h
%{_libdir}/%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

%files -n %{libev}
%{_libdir}/%{name}-libev.so.%{major}*

%files -n %{devev}
%{_includedir}/verto-libev.h
%{_libdir}/%{name}-libev.so
%{_libdir}/pkgconfig/%{name}-libev.pc

%files -n %{libevent}
%{_libdir}/%{name}-libevent.so.%{major}*

%files -n %{devevent}
%{_includedir}/verto-libevent.h
%{_libdir}/%{name}-libevent.so
%{_libdir}/pkgconfig/%{name}-libevent.pc

%if !%{with crosscompile}
%files -n %{libtevent}
%{_libdir}/%{name}-tevent.so.%{major}*

%files -n %{devtevent}
%{_includedir}/verto-tevent.h
%{_libdir}/%{name}-tevent.so
%{_libdir}/pkgconfig/%{name}-tevent.pc
%endif

