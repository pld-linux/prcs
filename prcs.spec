Summary:	Project Revision Control System
Name:		prcs
Version:	1.2.15
Release:	1
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
URL:		http://www.XCF.Berkeley.EDU/~jmacd/prcs.html
Source0:	ftp://ftp.XCF.Berkeley.EDU/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-el.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-rprcs-ssh.patch
BuildRequires:	libstdc++-devel
BuildRequires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PRCS is a simplified directory tree project oriented revision control
system.

%package el
Summary:	PRCS mode for EMACS
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Requires:	%{name} = %{version}
Requires:	xemacs

%description el
PRCS mode for EMACS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/* $RPM_BUILD_ROOT%{_mandir}/man1/
install scripts/rprcs $RPM_BUILD_ROOT%{_bindir}

gzip -9nf ANNOUNCE AUTHORS NEWS README FAQ ChangeLog \
	scripts/rprcs_session.log scripts/README.rprcs

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir

%postun
%fix_info_dir

%files
%defattr(644,root,root,755)
%doc *.gz scripts/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*

%files el
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-lisp/*
