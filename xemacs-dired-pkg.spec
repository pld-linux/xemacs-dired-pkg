Summary:	Manage file systems
Summary(pl):	Manager plik�w
Name:		xemacs-dired-pkg
%define 	srcname	dired
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
URL:		http://www.xemacs.org/
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	be9971fc8b39136a495a1a06110bc964
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg

%description
The DIRectory EDitor is for manipulating, and running commands on
files in a directory.

%description -l pl
Modu� do do zarz�dzania plikami.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/dired/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
