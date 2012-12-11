%define upstream_name    Net-Dropbox-API
%define upstream_version 1.7

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A dropbox API interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Random)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(JSON)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Net::OAuth)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(common::sense)
BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Dec 12 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 740506
- imported package perl-Net-Dropbox-API

