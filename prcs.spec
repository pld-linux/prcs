Summary:	Project Revision Control System
Summary(pl):	System kontroli wersji dla projektów
Name:		prcs
Version:	1.2.15
Release:	2
License:	GPL
Group:		Development/Version Control
Group(cs):	Vývojové prostøedky/Správ verzí
Group(da):	Udvikling/Versionskontrol
Group(de):	Entwicklung/Versionkontrolle
Group(es):	Desarrollo/Control de Versiones
Group(fr):	Development/Contrôle de version
Group(is):	Þróunartól/Útgáfu Stýring
Group(it):	Sviluppo/Controllo della versione
Group(no):	Utvikling/Versjonskontroll
Group(pl):	Programowanie/Zarz±dzanie wersjami
Group(pt):	Desenvolvimento/Controlo de Versões
Group(ru):	òÁÚÒÁÂÏÔËÁ/ëÏÎÔÒÏÌØ ×ÅÒÓÉÊ
Group(sl):	Razvoj/Nadzor razlièic
Group(sv):	Utveckling/Versionshantering
URL:		http://www.XCF.Berkeley.EDU/~jmacd/prcs.html
Source0:	ftp://ftp.XCF.Berkeley.EDU/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-el.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-r%{name}-ssh.patch
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

%package el
Summary:	PRCS mode for EMACS
Summary(pl):	Tryb PRCS dla EMACS-a
Group:		Development/Version Control
Group(cs):	Vývojové prostøedky/Správ verzí
Group(da):	Udvikling/Versionskontrol
Group(de):	Entwicklung/Versionkontrolle
Group(es):	Desarrollo/Control de Versiones
Group(fr):	Development/Contrôle de version
Group(is):	Þróunartól/Útgáfu Stýring
Group(it):	Sviluppo/Controllo della versione
Group(no):	Utvikling/Versjonskontroll
Group(pl):	Programowanie/Zarz±dzanie wersjami
Group(pt):	Desenvolvimento/Controlo de Versões
Group(ru):	òÁÚÒÁÂÏÔËÁ/ëÏÎÔÒÏÌØ ×ÅÒÓÉÊ
Group(sl):	Razvoj/Nadzor razlièic
Group(sv):	Utveckling/Versionshantering
Requires:	%{name} = %{version}
Requires:	xemacs

%description el
PRCS mode for EMACS.

%description el -l pl
Tryb PRCS dla EMACS-a.

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

install man/* $RPM_BUILD_ROOT%{_mandir}/man1
install scripts/rprcs $RPM_BUILD_ROOT%{_bindir}

gzip -9nf ANNOUNCE AUTHORS NEWS README FAQ ChangeLog \
	scripts/rprcs_session.log scripts/README.rprcs

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz scripts/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*

%files el
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-lisp/*
