Name:           rdo-testing
Version:        kilo
Release:        0.11
Summary:        RDO repository configuration
Conflicts:      rdo-release

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/redhat-openstack/rdo-release
Source0:        rdo-testing.repo

BuildArch:      noarch

%description
This package contains the RDO testing repository

%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-testing.repo

%files
%{_sysconfdir}/yum.repos.d/*.repo

%post

# Adjust repos as per dist and version

source /etc/os-release
DIST=$ID
RELEASEVER=$VERSION_ID

if [ "$DIST" != 'fedora' ]; then
  DIST=el
  FDIST=el
  # $releasever doesn't seem to be a reliable way to get the major version on RHEL
  # e.g. if distroverpkg isn't present in yum.conf mine was set to 6Server
  # because this was the version of the package redhat-release-server-6Server
  RELEASEVER=$(sed -e 's/.*release \([0-9]\+\).*/\1/' /etc/system-release)
else
  FDIST=f
  echo "%{name} not available on $DIST"
  exit 1
fi

for repo in rdo-testing ; do
  for var in DIST FDIST RELEASEVER; do
    sed -i -e "s/%$var%/$(eval echo \$$var)/g" %{_sysconfdir}/yum.repos.d/$repo.repo
  done
done

%changelog
* Tue May 05 2015 Alan Pevec <apevec@redhat.com> - kilo-0.11
- kilo testing
