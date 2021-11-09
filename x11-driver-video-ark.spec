%define _disable_ld_no_undefined 1 

Summary:	X.org driver for ARK Logic graphics chipsets
Name:		x11-driver-video-ark
Version:	0.7.5
Release:	18
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ark-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-ark is the X.org driver for ARK Logic graphics chipsets.

%prep
%setup -qn xf86-video-ark-%{version}
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ark_drv.so

