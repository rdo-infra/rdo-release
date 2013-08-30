Name:           rdo-release
Version:        havana
Release:        5
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            http://repos.fedorapeople.org/repos/openstack/
Source0:        rdo-release.repo
Source1:        RPM-GPG-KEY-RDO-Havana
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
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RDO-Havana
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
if ! grep -qFi 'fedora' /etc/redhat-release; then
  DIST=epel # Should this be something else (maybe el)?
  FDIST=el
  # $releasever doesn't seem to be a reliable way to get the major version on RHEL
  # e.g. if distroverpkg isn't present in yum.conf mine was set to 6Server
  # because this was the version of the package redhat-release-server-6Server
  RELEASEVER=$(sed -e 's/.*release \([0-9]\+\).*/\1/' /etc/redhat-release)
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
* Fri Aug 30 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-havana-5
- Revert Requires: on foreman-release
- Add references to foreman and puppetlabs repositories

* Sun Aug  4 2013 Pádraig Brady <pbrady@redhat.com> - rdo-release-havana-3
- Don't skip the RDO repo if unavailable
- Depend on foreman-release

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
