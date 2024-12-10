%define upstream_name    XS-Parse-Keyword

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.47
Release:    1

Summary:    Build-time support for C<XS::Parse::Keyword>
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-%{version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::CChecker)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword
plugins using the 'PL_keyword_plugin' hook mechanism. It is unlikely to be
of much use to anyone else; and highly unlikely to be any use when writing
perl code using these. Unless you are writing a keyword plugin using XS,
this module is not for you.

This module is also currently experimental, and the design is still
evolving and subject to change. Later versions may break ABI compatibility,
requiring changes or at least a rebuild of any module that depends on it.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorarch/*
