%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-ec2api

Name:                   puppet-ec2api
Version:                17.4.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack EC2 API Service
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-ec2api

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 4.0.0

%description
Installs and configures OpenStack EC2 API Service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ec2api/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ec2api/



%files
%{_datadir}/openstack-puppet/modules/ec2api/


%changelog
* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 17.4.0-1
- Update to 17.4.0



