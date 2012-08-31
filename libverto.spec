%define major 1


%define libverto %mklibname verto %{major}
%define develverto %mklibname verto -d
%define libglib %mklibname glib
%define libglibdevel %mklibname glib -d
%define libev %mklibname ev
%define libevdevel %mklibname ev -d
%define	libtevent %mklibname tevent
%define	libteventdevel %mklibname tevent -d
%define libevent %mklibname event
%define libeventdevel %mklibname event -d

Name:		libverto
Version:	0.2.4
Release:	3
Summary:	Main loop abstraction library
Group:		System/Libraries
License:	MIT
URL:		https://fedorahosted.org/libverto/
Source0:	http://fedorahosted.org/releases/l/i/%{name}/%{name}-%{version}.tar.gz
Patch1:		libverto-0.2.4-fix-libev.patch

BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(libev)
BuildRequires:	libevent-devel
BuildRequires:	tevent-devel

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


%package   -n	%libverto
Summary:	System libraries for %{name}
Group:		System/Libraries

%description -n %libverto
The %{name} package contains libraries for %{name}.


%package   -n	%develverto
Summary:	Development files for %{name}
Requires:	%{libverto} = %{version}-%{release}
Group:		Development/C 

%description -n %develverto
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	%libglib
Summary:	glib module for %{name}
Group:		System/Libraries
Requires:	%{libverto} = %{version}-%{release}

%description -n %libglib
Module for %{name} which provides integration with glib.

This package does NOT yet provide %{name}-module-base.

%package  -n	%libglibdevel
Summary:        Development files for %{name}-glib
Requires:       %{libglib} = %{version}-%{release}
Requires:       %{develverto} = %{version}-%{release}
Group:		Development/C 

%description -n %libglibdevel
The %{name}-glib-devel package contains libraries and header files for
developing applications that use %{name}-glib.

%package -n     %libev
Summary:        libev module for %{name}
Requires:       %{libverto} = %{version}-%{release}
Group:		System/Libraries
Provides:       %{name}-module-base = %{version}-%{release}

%description -n %libev
Module for %{name} which provides integration with libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n    %libevdevel
Summary:        Development files for %{name}-libev
Requires:       %{libev} = %{version}-%{release}
Requires:       %{develverto} = %{version}-%{release}
Group:		Development/C 

%description -n %libevdevel
The %{name}-libev-devel package contains libraries and header files for
developing applications that use %{name}-libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n    %libevent
Summary:        libevent module for %{name}
Requires:       %{libverto} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}
Group:		System/Libraries

%description -n %libevent
Module for %{name} which provides integration with libevent.

%package   -n   %libeventdevel
Summary:        Development files for %{name}-libevent
Requires:       %{libevent} = %{version}-%{release}
Requires:       %{develverto} = %{version}-%{release}
Group:		Development/C 

%description -n %libeventdevel
The %{name}-libevent-devel package contains libraries and header files for
developing applications that use %{name}-libevent.

%package   -n   %libtevent
Summary:        tevent module for %{name}
Requires:       %{libverto} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}
Group:		System/Libraries

%description -n   %libtevent
Module for %{name} which provides integration with tevent.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package  -n	%libteventdevel
Summary:        Development files for %{name}-tevent
Requires:       %{libtevent} = %{version}-%{release}
Requires:       %{develverto} = %{version}-%{release}
Group:		Development/C 

%description -n %libteventdevel
The %{name}-tevent-devel package contains libraries and header files for
developing applications that use %{name}-tevent.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fi
%configure --disable-static
make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog COPYING NEWS README

%files -n %{libverto}
%{_libdir}/%{name}.so.*

%files -n %develverto
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %libglib
%{_libdir}/%{name}-glib.so.*

%files -n %libglibdevel
%{_includedir}/verto-glib.h
%{_libdir}/%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

%files -n %libev
%{_libdir}/%{name}-libev.so.*

%files -n %libevdevel
%{_includedir}/verto-libev.h
%{_libdir}/%{name}-libev.so
%{_libdir}/pkgconfig/%{name}-libev.pc

%files -n %libevent
%{_libdir}/%{name}-libevent.so.*

%files -n %libeventdevel
%{_includedir}/verto-libevent.h
%{_libdir}/%{name}-libevent.so
%{_libdir}/pkgconfig/%{name}-libevent.pc

%files -n %libtevent
%{_libdir}/%{name}-tevent.so.*

%files -n %libteventdevel
%{_includedir}/verto-tevent.h
%{_libdir}/%{name}-tevent.so
%{_libdir}/pkgconfig/%{name}-tevent.pc
