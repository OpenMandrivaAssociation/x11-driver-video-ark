Name: x11-driver-video-ark
Version: 0.7.5
Release: 2
Summary: X.org driver for ARK Logic graphics chipsets
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ark-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-ark is the X.org driver for ARK Logic graphics chipsets.

%prep
%setup -qn xf86-video-ark-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/ark_drv.so



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.5-1
+ Revision: 810720
- version update 0.7.5

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.7.4-1
+ Revision: 787193
- Update to 0.7.4
- Build for xorg 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.7.3-7
+ Revision: 748369
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.3-6
+ Revision: 703648
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.7.3-5
+ Revision: 683560
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-4
+ Revision: 671139
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.7.3-3mdv2011.0
+ Revision: 595740
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Jul 26 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.7.3-1mdv2011.0
+ Revision: 560862
- New version: 0.7.3

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 432151
- new release

* Tue Aug 11 2009 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.0
+ Revision: 414540
- use configure2_5x

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 0.7.1-1mdv2009.1
+ Revision: 317837
- New version 0.7.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.0-3mdv2009.1
+ Revision: 308212
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-2mdv2009.0
+ Revision: 265901
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.7.0-1mdv2009.0
+ Revision: 194216
- Update to version 0.7.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.6.0-7mdv2008.1
+ Revision: 165478
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.6.0-6mdv2008.1
+ Revision: 156597
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.6.0-5mdv2008.1
+ Revision: 154932
- Don't need to check for dri headers and run time
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-ark-0.6.0@mandriva suggested on upstream
  Tag at git checkout f09baa348b5d1a499f23e553c67bc0674c7c6512
  Note that there is a tag named ark-0_6_0, but the local tag matches
  a more wider naming pattern among other repositories and includes harmless
  updates (addition of .gitignore, .cvsignore and change to use macros instead
  of static values to specifiy package version)
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.6.0-4mdv2008.1
+ Revision: 98684
- minor spec cleanup
- build against new xserver (1.4)

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-3mdv2008.0
+ Revision: 75721
- rebuild

