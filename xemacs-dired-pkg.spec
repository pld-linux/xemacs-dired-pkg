Summary:	Manage file systems
Summary(pl.UTF-8):	Manager plików
Name:		xemacs-dired-pkg
%define 	srcname	dired
Version:	1.20
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
URL:		http://www.xemacs.org/
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	6d7a66868d968d259dbb6a8f7376b78b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg

%description
The DIRectory EDitor is for manipulating, and running commands on
files in a directory.

%description -l pl.UTF-8
Moduł do do zarządzania plikami.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/dired/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
