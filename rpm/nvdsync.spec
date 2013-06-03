%define name		nvdsync
%define release		1
%define version 	0.2
%define mybuilddir	${HOME}/redhat/BUILD/%{name}-%{version}-root

Requires:		bash, curl, nvd2sqlite3, nvdXjira
BuildRoot:		%{mybuilddir}
BuildArch:		noarch
Summary:		fetch NIST's NVD, sync into a local database and cross-reference with Jira
License: 		BSD
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr
Group: 			Development/Tools

%description
The nvdsync utility wraps the nvd2sqlite3 and nvdXjira tools to provide a
simple script suitable to be run from a cronjob in order to fetch NIST's
National Vulnerability Database, sync it into a local sqlite3 database and
then cross-reference that database with a Jira instance.

%prep
%setup -q

%build
mkdir -p %{mybuilddir}/usr/bin
mkdir -p %{mybuilddir}/usr/share/man/man1

%install
install -c -m 755 src/nvdsync %{mybuilddir}/usr/bin/nvdsync
install -c -m 444 doc/nvdsync.1 %{mybuilddir}/usr/share/man/man1/nvdsync.1

%files
%defattr(0444,root,root)
%attr(0755,root,root) /usr/bin/nvdsync
%doc /usr/share/man/man1/nvdsync.1.gz

%changelog
* Mon May 06 2013 - jschauma@netmeister.org
- 0.2
-  accept CURL_FLAGS
-  fix usage

* Fri May 03 2013 - jschauma@netmeister.org
- 0.1:
-  initial version
