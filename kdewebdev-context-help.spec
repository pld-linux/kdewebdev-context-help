Summary:	Context help for CSS, HTML, JS, MySQL and PHP in Quanta
Summary(pl):	Pomoc kontekstowa Quanty dla CSS, HTML, JS, MySQL i PHP
Name:		kdewebdev-context-help
Version:	0.20041123
Release:	1
Epoch:		0
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/quanta/css.tar.bz2
# Source0-md5:	365401c41fbefe56c05a5bd16e0d7354
Source1:	http://dl.sourceforge.net/quanta/html.tar.bz2
# Source1-md5:	2be9c55d9795faa46cb094a1919e9c89
Source2:	http://dl.sourceforge.net/quanta/javascript.tar.bz2
# Source2-md5:	4e4945ac5b842339ecc69b4c63960529
Source3:	http://dl.sourceforge.net/quanta/mysql-20030405.tar.bz2
# Source3-md5:	5724096006900495e07a46e8dbd22bbd
Source4:	http://dl.sourceforge.net/quanta/php.tar.bz2
# Source4-md5:	2d19a72114cce1485c1c23ff28135210
BuildRequires:	tar >= 1:1.15.1
Requires:	kdewebdev-quanta
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qhelpdir	%{_datadir}/apps/quanta/doc

%description
This package provides context help for CSS, HTML, JS, MySQL and PHP.

%description -l pl
Ten pakiet dostarcza pomoc kontekstow± dla CSS, HTML, JS, MySQL i PHP.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{qhelpdir}

bzip2 -dc %{SOURCE0} | tar -xf - --strip-components=1 -C $RPM_BUILD_ROOT%{qhelpdir}
bzip2 -dc %{SOURCE1} | tar -xf - --strip-components=1 -C $RPM_BUILD_ROOT%{qhelpdir}
bzip2 -dc %{SOURCE2} | tar -xf - --strip-components=1 -C $RPM_BUILD_ROOT%{qhelpdir}
bzip2 -dc %{SOURCE3} | tar -xf - --strip-components=1 -C $RPM_BUILD_ROOT%{qhelpdir}
bzip2 -dc %{SOURCE4} | tar -xf - --strip-components=1 -C $RPM_BUILD_ROOT%{qhelpdir}

rm $RPM_BUILD_ROOT%{qhelpdir}/*.sh
rm $RPM_BUILD_ROOT%{qhelpdir}/*.kmdr
rm $RPM_BUILD_ROOT%{qhelpdir}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{qhelpdir}/*.docrc
%{qhelpdir}/css
%{qhelpdir}/html
%{qhelpdir}/javascript
%{qhelpdir}/mysql
%{qhelpdir}/php
