Name:           rdo-release
#Version:        7
# setting Version to grizzly may be a bad idea, but it makes it clear to the user
# that is is the grizzly version without having to change the package name
# Alternativly I would set it to 7 (8 = Havana etc...)
Version:        grizzly
Release:        4
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            http://repos.fedorapeople.org/repos/openstack/
Source0:        rdo-release.repo
Source1:        RPM-GPG-KEY-RDO-Grizzly

BuildArch:      noarch

Requires:       foreman-release

%description
This package contains the RDO repository

%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-release.repo

#GPG Key
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Grizzly

%files
%{_sysconfdir}/yum.repos.d/rdo-release.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Grizzly

%post

# set baseurl (will this be moved to rdo url)
# baseurl=http://repos.fedorapeople.org/repos/openstack/openstack-grizzly/fedora-$releasever/
# baseurl=http://repos.fedorapeople.org/repos/openstack/openstack-grizzly/epel-6/

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
* Sun Aug  4 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-grizzly-4
- Don't skip the RDO repo if unavailable
- Depend on foreman-release

* Thu May 09 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-grizzly-3
- Remove dependency on yum-plugin-priorities, to avoid optional repo dependency

* Thu Apr 25 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-grizzly-2
- Depend on yum-plugin-priorities
- Enable GPG key by default

* Tue Apr 09 2013 Martin Mágr <mmagr@redhat.com> - rdo-release-grizzly-1
- Added GPG key

* Wed Mar 27 2013 Derek Higgins <derekh@redhat.com> - rdo-release-grizzly-1
- Creating Package
