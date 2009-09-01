# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	Asterisk-Stat : CDR Analyser
Name:		asterisk-stat
Version:	2.0.1
Release:	%mkrel 5
License:	GPL
Group:		System/Servers
URL:		http://areski.net/asterisk-stat-v2/about.php
Source0:	http://areski.net/asterisk-stat-v2/%{name}-v2_0_1.tar.bz2
Patch0:		asterisk-stat-mdk_conf.diff
Requires:	webserver
Requires:	php-common
Requires:	php-mysql
Requires:	php-gd
Requires:	mod_php
BuildRequires:	file
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Asterisk-Stat is providing different reports & Graph to allow
the Asterisk-admin to analyse quickly and easily the traffic on
their Asterisk server. All the graphic & reports are based over
the CDR database. 

%prep

%setup -q -n %{name}-v2
%patch0 -p0

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_var}/www/html/%{name}
cp -aRf * %{buildroot}%{_var}/www/html/%{name}/

# cleanup
rm -rf %{buildroot}%{_var}/www/html/%{name}/CHANGELOG.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/counter.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/info.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/wiki.html

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG.txt
%config(noreplace) %attr(0644,root,root) %{_var}/www/html/%{name}/lib/defines.php
%{_var}/www/html/%{name}
