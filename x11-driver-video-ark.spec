%define _disable_ld_no_undefined 1
%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration

Summary:	X.org driver for ARK Logic graphics chipsets
Name:		x11-driver-video-ark
Version:	0.7.6
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-ark-%{version}.tar.xz

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
%make_build

%install
%make_install

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ark_drv.so

