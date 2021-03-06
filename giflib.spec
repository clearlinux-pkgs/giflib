#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : giflib
Version  : 5.2.1
Release  : 5
URL      : https://sourceforge.net/projects/giflib/files/giflib-5.2.1.tar.gz
Source0  : https://sourceforge.net/projects/giflib/files/giflib-5.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: giflib-bin = %{version}-%{release}
Requires: giflib-lib = %{version}-%{release}
Requires: giflib-license = %{version}-%{release}
Requires: giflib-man = %{version}-%{release}
BuildRequires : xmlto

%description
= GIFLIB =
Latest versions of GIFLIB are currently hosted at:
http://sourceforge.net/projects/giflib

%package bin
Summary: bin components for the giflib package.
Group: Binaries
Requires: giflib-license = %{version}-%{release}

%description bin
bin components for the giflib package.


%package dev
Summary: dev components for the giflib package.
Group: Development
Requires: giflib-lib = %{version}-%{release}
Requires: giflib-bin = %{version}-%{release}
Provides: giflib-devel = %{version}-%{release}
Requires: giflib = %{version}-%{release}

%description dev
dev components for the giflib package.


%package lib
Summary: lib components for the giflib package.
Group: Libraries
Requires: giflib-license = %{version}-%{release}

%description lib
lib components for the giflib package.


%package license
Summary: license components for the giflib package.
Group: Default

%description license
license components for the giflib package.


%package man
Summary: man components for the giflib package.
Group: Default

%description man
man components for the giflib package.


%package staticdev
Summary: staticdev components for the giflib package.
Group: Default
Requires: giflib-dev = %{version}-%{release}

%description staticdev
staticdev components for the giflib package.


%prep
%setup -q -n giflib-5.2.1
cd %{_builddir}/giflib-5.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605556807
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  all


%install
export SOURCE_DATE_EPOCH=1605556807
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/giflib
cp %{_builddir}/giflib-5.2.1/COPYING %{buildroot}/usr/share/package-licenses/giflib/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1
make install DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=/usr/lib64

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gif2rgb
/usr/bin/gifbuild
/usr/bin/gifclrmp
/usr/bin/giffix
/usr/bin/giftext
/usr/bin/giftool

%files dev
%defattr(-,root,root,-)
/usr/include/gif_lib.h
/usr/lib64/libgif.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgif.so.7
/usr/lib64/libgif.so.7.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/giflib/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gif2rgb.1
/usr/share/man/man1/gifbg.1
/usr/share/man/man1/gifbuild.1
/usr/share/man/man1/gifclrmp.1
/usr/share/man/man1/gifcolor.1
/usr/share/man/man1/gifecho.1
/usr/share/man/man1/giffix.1
/usr/share/man/man1/gifhisto.1
/usr/share/man/man1/gifinto.1
/usr/share/man/man1/giflib.1
/usr/share/man/man1/giftext.1
/usr/share/man/man1/giftool.1
/usr/share/man/man1/gifwedge.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgif.a
