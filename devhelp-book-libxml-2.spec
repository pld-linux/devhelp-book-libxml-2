Summary:	DevHelp book: libxml-2
Summary(pl):	Ksi±¿ka do DevHelp'a o libxml-2
Name:		devhelp-book-libxml-2
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libxml-2.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about libxml-2

%description -l pl
Ksi±¿ka do DevHelp o libxml-2

%prep
%setup -q -c libxml-2 -n libxml-2

%build
mv -f book libxml-2
mv -f book.devhelp libxml-2.devhelp
rm -rf libxml-2/CVS

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libxml-2
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install libxml-2.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install libxml-2/* $RPM_BUILD_ROOT%{_prefix}/books/libxml-2

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
