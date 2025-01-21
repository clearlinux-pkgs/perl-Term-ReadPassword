#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-ReadPassword
Version  : 0.11
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/P/PH/PHOENIX/Term-ReadPassword-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PH/PHOENIX/Term-ReadPassword-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libterm-readpassword-perl/libterm-readpassword-perl_0.11-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Term-ReadPassword-license = %{version}-%{release}
Requires: perl-Term-ReadPassword-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This module is in alpha-testing. Build in the usual way; send bug reports
and patches to me at the address below. From the documentation:

%package dev
Summary: dev components for the perl-Term-ReadPassword package.
Group: Development
Provides: perl-Term-ReadPassword-devel = %{version}-%{release}
Requires: perl-Term-ReadPassword = %{version}-%{release}

%description dev
dev components for the perl-Term-ReadPassword package.


%package license
Summary: license components for the perl-Term-ReadPassword package.
Group: Default

%description license
license components for the perl-Term-ReadPassword package.


%package perl
Summary: perl components for the perl-Term-ReadPassword package.
Group: Default
Requires: perl-Term-ReadPassword = %{version}-%{release}

%description perl
perl components for the perl-Term-ReadPassword package.


%prep
%setup -q -n Term-ReadPassword-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libterm-readpassword-perl_0.11-3.debian.tar.xz
cd %{_builddir}/Term-ReadPassword-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Term-ReadPassword-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Term-ReadPassword
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Term-ReadPassword/329ef92ca26e682ea3d1dd1808862437fdb74bac
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::ReadPassword.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Term-ReadPassword/329ef92ca26e682ea3d1dd1808862437fdb74bac

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
