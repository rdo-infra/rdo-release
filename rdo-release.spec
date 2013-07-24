Name:           rdo-release
Version:        havana
Release:        2
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            http://repos.fedorapeople.org/repos/openstack/
Source0:        rdo-release.repo
Source1:        RPM-GPG-KEY-RDO-Havana

BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-release.repo

#GPG Key
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Havana

%files
%{_sysconfdir}/yum.repos.d/rdo-release.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Havana

%post

# set baseurl
# baseurl=http://rdo.fedorapeople.org/openstack/openstack-havana/fedora-$releasever/
# baseurl=http://rdo.fedorapeople.org/openstack/openstack-havana/epel-6/

DIST=fedora
RELEASEVER='$releasever'
grep -i fedora /etc/redhat-release > /dev/null
if [ $? != 0 ] ; then
    DIST=epel # Should this be something else (maybe el)?
    # $releasever doesn't seem to be a reliable way to get the major version on RHEL
    # e.g. if distroverpkg isn't present in yum.conf mine was set to 6Server
    # because this was the version of the package redhat-release-server-6Server
    RELEASEVER=$(sed -e 's/.*release \([0-9]\+\).*/\1/' /etc/redhat-release)
fi

sed -i -e "s/%DIST%/$DIST/g" %{_sysconfdir}/yum.repos.d/rdo-release.repo
sed -i -e "s/%RELEASEVER%/$RELEASEVER/g" %{_sysconfdir}/yum.repos.d/rdo-release.repo

%changelog
* Tue Jul 23 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-havana-2
- Update to Havana

* Thu May 09 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-grizzly-3
- Remove dependency on yum-plugin-priorities, to avoid optional repo dependency

* Thu Apr 25 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-grizzly-2
- Depend on yum-plugin-priorities
- Enable GPG key by default

* Tue Apr 09 2013 Martin Mágr <mmagr@redhat.com> - rdo-release-grizzly-1
- Added GPG key

* Wed Mar 27 2013 Derek Higgins <derekh@redhat.com> - rdo-release-grizzly-1
- Creating Package
