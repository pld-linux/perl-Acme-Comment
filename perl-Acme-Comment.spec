#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Acme
%define	pnam	Comment
Summary:	Acme::Comment
Name:		perl-Acme-Comment
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Acme/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b005f8a9849949b8a3b9392cd3fd90bd
URL:		http://search.cpan.org/dist/Acme-Comment/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acme::Comment allows multi-line comments which are filtered out.
Unlike the pseudo multi-line comment if (0) {}, the code being
commented out need not be syntactically valid.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%dir %{perl_vendorlib}/Acme
%{perl_vendorlib}/Acme/*.pm
%{_mandir}/man3/*
