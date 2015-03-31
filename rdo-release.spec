Name:           rdo-release
Version:        icehouse
Release:        4.1
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/redhat-openstack/rdo-release
Source0:        rdo-release.repo
Source1:        RPM-GPG-KEY-RDO-Icehouse
Source2:        foreman.repo
Source3:        RPM-GPG-KEY-foreman
Source4:        puppetlabs.repo
Source5:        RPM-GPG-KEY-puppetlabs

BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-release.repo
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d/foreman.repo
install -p -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/yum.repos.d/puppetlabs.repo

#GPG Keys
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Icehouse
install -Dpm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman
install -Dpm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-puppetlabs

%files
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-*

%post

# Adjust repos as per dist and version

DIST=fedora
FDIST=f
RELEASEVER='$releasever'
if ! grep -qFi 'fedora' /etc/system-release; then
  DIST=epel # Should this be something else (maybe el)?
  FDIST=el
  # $releasever doesn't seem to be a reliable way to get the major version on RHEL
  # e.g. if distroverpkg isn't present in yum.conf mine was set to 6Server
  # because this was the version of the package redhat-release-server-6Server
  RELEASEVER=$(sed -e 's/.*release \([0-9]\+\).*/\1/' /etc/system-release)
fi

# foreman isn't currrently supported on Fedora.
# Furthermore there isn't even an f20 dir on yum.theforeman.org
# So just avoid the foreman repos on fedora for now
# Also the rails version on el7 is currently not supported by theforeman,
# so disable there also.
if [ "$DIST" = 'fedora' ] || [ "$RELEASEVER" -ge 7 ]; then
  sed -i -e 's/enabled=1/enabled=0/' %{_sysconfdir}/yum.repos.d/foreman.repo
fi

# The puppetlabs EL7 repos look incomplete at present, so disable for now.
if [ "$DIST" = 'epel' ] && [ "$RELEASEVER" -ge 7 ]; then
  sed -i -e 's/enabled=1/enabled=0/' %{_sysconfdir}/yum.repos.d/puppetlabs.repo
fi

for repo in rdo-release foreman puppetlabs; do
  if [ "$repo" = "puppetlabs" ]; then
    [ "$DIST" = 'epel' ] && DIST=$FDIST
    [ "$DIST" = 'fedora' ] && RELEASEVER=$FDIST$RELEASEVER
  fi
  for var in DIST FDIST RELEASEVER; do
    sed -i -e "s/%$var%/$(eval echo \$$var)/g" %{_sysconfdir}/yum.repos.d/$repo.repo
  done
done

%changelog
* Wed Apr 01 2015 Alan Pevec <apevec@redhat.com> - icehouse-4.1
- fix for CentOS 7.1 redhat-release split

* Wed Jul 09 2014 Pádraig Brady <pbrady@redhat.com> - icehouse-4
- Update the foreman GPG key which changed mid release

* Tue Apr 22 2014 Pádraig Brady <pbrady@redhat.com> - icehouse-3
- Link to foreman 1.5 which is compatible with puppet >= 3.5.1

* Mon Mar 03 2014 Pádraig Brady <pbrady@redhat.com> - icehouse-2
- Disable the foreman repos on EL7

* Mon Jan 06 2014 Pádraig Brady <pbrady@redhat.com> - icehouse-1
- Update to Icehouse
- Disable the foreman repos on Fedora

* Wed Oct 23 2013 Pádraig Brady <pbrady@redhat.com> - havana-7
- Reference latest stable foreman release (1.3)

* Fri Aug 30 2013 Pádraig Brady <pbrady@redhat.com> - havana-6
- Revert Requires: on foreman-release
- Add references to foreman and puppetlabs repositories

* Sun Aug  4 2013 Pádraig Brady <pbrady@redhat.com> - havana-3
- Don't skip the RDO repo if unavailable
- Depend on foreman-release

* Tue Jul 23 2013 Pádraig Brady <pbrady@redhat.com> - havana-2
- Update to Havana

* Thu May 09 2013 Pádraig Brady <pbrady@redhat.com> - grizzly-3
- Remove dependency on yum-plugin-priorities, to avoid optional repo dependency

* Thu Apr 25 2013 Pádraig Brady <pbrady@redhat.com> - grizzly-2
- Depend on yum-plugin-priorities
- Enable GPG key by default

* Tue Apr 09 2013 Martin Mágr <mmagr@redhat.com> - grizzly-1
- Added GPG key

* Wed Mar 27 2013 Derek Higgins <derekh@redhat.com> - grizzly-1
- Creating Package
