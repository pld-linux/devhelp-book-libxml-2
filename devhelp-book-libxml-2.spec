Summary:	DevHelp book: libxml2
Summary(pl):	Ksi±¿ka do DevHelpa o libxml2
Name:		devhelp-book-libxml-2
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libxml-2.tar.gz
# Source0-md5:	22027287e8da74a8ccf33b5f101fac39
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about libxml2.

%description -l pl
Ksi±¿ka do DevHelpa o libxml-2.

%prep
%setup -q -c -n libxml-2

rm -rf book/CVS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/libxml-2,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/libxml-2.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libxml-2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
