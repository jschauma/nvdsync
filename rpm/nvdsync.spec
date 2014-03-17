%define name		nvdsync
%define release		1
%define version 	0.7
%define mybuilddir	${HOME}/redhat/BUILD/%{name}-%{version}-root

Requires:		bash, nvdXjira, wget
BuildRoot:		%{mybuilddir}
BuildArch:		noarch
Summary:		fetch NIST's NVD and cross-reference with Jira
License: 		BSD
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr
Group: 			Development/Tools

%description
The nvdsync utility wraps the nvdXjira tool to provide a simple script
suitable to be run from a cronjob in order to fetch NIST's National
Vulnerability Database, and then cross-reference that database with a Jira
instance.

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
* Fri Mar 14 2014 - jschauma@twitter.com
- 0.7
-  NIST changed the location of the feeds


* Wed Mar 12 2014 - jschauma@twitter.com
- 0.6.1
-  minor fix for [SECURITY-11696]: eval wget invocation to properly expand
   all flags

* Tue Mar 11 2014 - jschauma@twitter.com
- 0.6
-  [SECURITY-11696]: use wget(1) instead of curl(1) to work around a bug
   in some versions of curl(1) where it can't validate an SSL certificate
   signed using SHA-256

* Mon Feb 10 2014 - jschauma@twitter.com
- 0.5
-  use https for recent XML list
-  properly report URL in error messages

* Mon Oct 28 2013 - jschauma@twitter.com
- 0.4
-  [SECURITY-10345]: drop support for nvd2sqlite3

* Tue Sep 17 2013 - jschauma@twitter.com
- 0.3
-  [SECURITY-9860]: update location of NIST feed
-  [SECURITY-9860]: detect and bail out on HTTP errors when fetching NIST
   feed

* Mon May 06 2013 - jschauma@twitter.com
- 0.2
-  accept CURL_FLAGS
-  fix usage

* Fri May 03 2013 - jschauma@twitter.com
- 0.1:
-  initial version
