Summary:	Project Revision Control System
Summary(pl.UTF-8):	System kontroli wersji dla projektów
Name:		prcs
Version:	1.3.2
Release:	3
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e18a0566d512ea4ef7018a9b4158ff8f
Patch0:		%{name}-man.patch
Patch1:		%{name}-perl.patch
Patch2:		%{name}-gcc3.patch
URL:		http://prcs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	xemacs-ediff-pkg
BuildRequires:	xemacs-emerge-pkg
BuildRequires:	xemacs-vc-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PRCS is a simplified directory tree project oriented revision control
system.

%description -l pl.UTF-8
PRCS to uproszczony, zorientowany na drzewo katalogowe system kontroli
wersji.

%package -n xemacs-prcs-pkg
Summary:	PRCS mode for EMACS
Summary(pl.UTF-8):	Tryb PRCS dla EMACS-a
Group:		Development/Version Control
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs
Obsoletes:	prcs-el

%description -n xemacs-prcs-pkg
PRCS mode for EMACS.

%description -n xemacs-prcs-pkg -l pl.UTF-8
Tryb PRCS dla EMACS-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f emacs/*.elc

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	SYS_RCS_COMMAND_PATH="/usr/bin/rcs" \
	SYS_CI_COMMAND_PATH="/usr/bin/ci" \
	SYS_CO_COMMAND_PATH="/usr/bin/co" \
	SYS_RLOG_COMMAND_PATH="/usr/bin/rlog"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	lispdir=%{_datadir}/xemacs/site-lisp

install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README README.BE FAQ ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*

%files -n xemacs-prcs-pkg
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-lisp/*
