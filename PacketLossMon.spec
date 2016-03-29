%define pkgname PacketLossMon
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

name:      PacketLossMon
summary:   PacketLossMon is a set of scripts that expands the use of a local zabbix agent to perform packet loss enumeration
version:   0.1
release:   1
vendor:    wepa
packager:  Izz Noland <izz.noland@wepanow.com>
license:   GPL
group:     Networking/Utilities
url:       http://www.wepanow.com
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: noarch
prefix:    %(echo %{_prefix})
requires:  ztc
requires:  zabbix-agent
source:    %{name}-%{version}.tar.gz

%description
None.


%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -D -m0644 files/packetloss.conf $RPM_BUILD_ROOT/etc/zabbix-agent.d/packetloss.conf
install -D -m0755 files/icmp_test.sh $RPM_BUILD_ROOT/usr/local/sbin/icmp_test.sh


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%post
test -e /etc/init.d/zabbix-agentd && /etc/init.d/zabbix-agentd status && /etc/init.d/zabbix-agentd restart

%files
%config(noreplace) /etc/zabbix-agent.d/packetloss.conf
/usr/local/sbin/icmp_test.sh


%changelog
* Tue Mar 29 2016 izz.noland@wepanow.com
- Initial build.
