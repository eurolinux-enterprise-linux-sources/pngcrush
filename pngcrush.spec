
%global         _hardened_build 1

Summary:        Optimizer for PNG (Portable Network Graphics) files
Name:           pngcrush
Version:        1.7.59
Release:        2%{?dist}
License:        zlib
Group:          Applications/File
URL:            http://pmt.sourceforge.net/pngcrush/
Source0:        http://downloads.sourceforge.net/pmt/%{name}-%{version}-nolib.tar.xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  libpng-devel, zlib-devel, pkgconfig

%description
%{pngcrush} is an optimizer for PNG (Portable Network Graphics) files. It can be
run from a commandline in an MSDOS window, or from a UNIX or LINUX commandline.

Its main purpose is to reduce the size of the PNG IDAT datastream by trying
various compression levels an PNG filter methods. It also can be used to
remove unwanted ancillary chunks, or to add certain chunks including gAMA,
tRNS, iCCP, and textual chunks. 

%prep
%setup -q -n %{name}-%{version}-nolib

%build
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h # force using system headers
pngflags=$(pkg-config --cflags --libs libpng)
gcc %{optflags} $pngflags -lz -o pngcrush pngcrush.c

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 pngcrush %{buildroot}%{_bindir}/pngcrush

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc ChangeLog.html
%{_bindir}/%{name}

%changelog
* Sun Jun  2 2013 François Cami <fcami@fedoraproject.org> - 1.7.59-2
- Switch to the smaller -nolib archive.

* Fri May 31 2013 François Cami <fcami@fedoraproject.org> - 1.7.59-1
- New upstream release.
- Use more macros.
- Switch to hardened build.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 François Cami <fcami@fedoraproject.org> - 1.7.43-1
- New upstream release.

* Tue Jul 31 2012 Jon Ciesla <limburgher@gmail.com> - 1.7.35-1
- Update to latest to fix FTBFS.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.6.10-8
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Gerd Hoffmann <kraxel@redhat.com> - 1.6.10-6
- Fix FTBFS (#565047).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 3 2008 - Gerd Hoffmann <kraxel@redhat.com> - 1.6.10-3.fc9
- remove all unneeded (zlib/libpng copy) header files.
- fix Source: URL.
- get cflags and libs from pkg-config.

* Fri Oct 31 2008 - Gerd Hoffmann <kraxel@redhat.com> - 1.6.10-2.fc9
- use $RPM_OPT_FLAGS.
- use systems zlib and libpng.

* Wed Oct 15 2008 - Gerd Hoffmann <kraxel@redhat.com> - 1.6.10-1.fc9
- update to 1.6.10.
- add dist tag to release.
- fix license.
- fix rpmlint warnings.

* Mon Jul 07 2008 - Patrick Steiner <patrick.steiner@a1.net> - 1.6.7-1
- Initial package.
