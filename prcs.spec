Summary:	Project Revision Control System
Summary(pl):	System kontroli wersji dla projektów
Name:		prcs
Version:	1.3.2
Release:	2
License:	GPL
Group:		Development/Version Control
URL:		http://prcs.sourceforge.net/
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}//%{name}-%{version}.tar.gz
Patch0:		%{name}-man.patch
Patch1:		%{name}-perl.patch
BuildRequires:	libstdc++-devel
BuildRequires:	xemacs
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PRCS is a simplified directory tree project oriented revision control
system.

%description -l pl
PRCS to uproszczony, zorientowany na drzewo katalogowe system kontroli
wersji.

%package -n xemacs-prcs-pkg
Summary:	PRCS mode for EMACS
Summary(pl):	Tryb PRCS dla EMACS-a
Group:		Development/Version Control
Requires:	%{name} = %{version}
Requires:	xemacs
Obsoletes:	prcs-el

%description -n xemacs-prcs-pkg
PRCS mode for EMACS.

%description -n xemacs-prcs-pkg -l pl
Tryb PRCS dla EMACS-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	lispdir=%{_datadir}/xemacs/site-lisp

install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README README.BE FAQ ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*

%files -n xemacs-prcs-pkg
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-lisp/*
