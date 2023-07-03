%define _empty_manifest_terminate_build 0
%define upstream_name    XS-Parse-Keyword
%define upstream_version 0.24

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Build-time support for C<XS::Parse::Keyword>
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/XS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::CChecker) >= 0.110.0
BuildRequires: perl(ExtUtils::ParseXS) >= 3.160.0
BuildRequires: perl(Module::Build) >= 0.400.400
BuildRequires: perl(Test::More) >= 0.880.0
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
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

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
