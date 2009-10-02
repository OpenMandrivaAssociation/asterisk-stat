Name:		asterisk-stat
Version:	2.0.1
Release:	%mkrel 6
Summary:	Asterisk-Stat : CDR Analyser
License:	GPL
Group:		System/Servers
URL:		http://areski.net/asterisk-stat-v2/about.php
Source0:	http://areski.net/asterisk-stat-v2/%{name}-v2_0_1.tar.bz2
Patch0:		asterisk-stat-mdk_conf.diff
Requires:	webserver
Requires:	php-mysql
Requires:	php-gd
Requires:	mod_php
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Asterisk-Stat is providing different reports & Graph to allow
the Asterisk-admin to analyse quickly and easily the traffic on
their Asterisk server. All the graphic & reports are based over
the CDR database. 

%prep
%setup -q -n %{name}-v2
%patch0 -p0

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_var}/www/html/%{name}
cp -aRf * %{buildroot}%{_var}/www/html/%{name}/

# cleanup
rm -rf %{buildroot}%{_var}/www/html/%{name}/CHANGELOG.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/counter.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/info.txt
rm -rf %{buildroot}%{_var}/www/html/%{name}/wiki.html

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG.txt
%config(noreplace) %attr(0644,root,root) %{_var}/www/html/%{name}/lib/defines.php
%{_var}/www/html/%{name}
