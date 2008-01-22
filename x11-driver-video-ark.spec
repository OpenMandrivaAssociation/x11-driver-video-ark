Name: x11-driver-video-ark
Version: 0.6.0
Release: %mkrel 6
Summary: The X.org driver for ARK Logic graphics chipsets
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-ark-0.6.0@mandriva suggested on upstream
# Tag at git checkout f09baa348b5d1a499f23e553c67bc0674c7c6512
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-ark  xorg/drivers/xf86-video-ark
# cd xorg/drivers/xf86-video/ark
# git-archive --format=tar --prefix=xf86-video-ark-0.6.0/ xf86-video-ark-0.6.0@mandriva | bzip2 -9 > xf86-video-ark-0.6.0.tar.bz2
########################################################################
Source0: xf86-video-ark-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-ark-0.6.0@mandriva..origin/mandriva
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Don-t-need-to-check-for-dri-headers-and-run-time.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for ARK Logic graphics chipsets

%prep
%setup -q -n xf86-video-ark-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/ark_drv.so
