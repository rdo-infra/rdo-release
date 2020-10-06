Name:           rdo-release
Version:        victoria
Release:        0%{?dist}
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/rdo-infra/rdo-release
# repository files
Source0001:     rdo-release.repo
Source0002:     rdo-testing.repo
# GPG keys
Source0101:     RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch:      noarch

Requires: centos-release
Requires: centos-release-advanced-virtualization
Requires: centos-release-rabbitmq-38
Requires: centos-release-ceph-nautilus
Requires: centos-release-nfv-openvswitch

%description
This package contains the RDO repository

%install
install -p -d %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d

#GPG Keys
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE101} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
* Mon Oct 05 2020 Yatin Karel <ykarel@redhat.com> - victoria-0
- Pre-release RDO Victoria repo setup for bootstraping Victoria CI

* Mon May 11 2020 Alfredo Moralejo <amoralej@redhat.com> - ussuri-1
- Enable RDO Ussuri released repo and disable testing one.

* Thu May 07 2020 Yatin Karel <ykarel@redhat.com> - ussuri-0
- Pre-release RDO Ussuri repo setup for bootstraping Ussuri CI

* Mon Apr 13 2020 Alfredo Moralejo <amoralej@redhat.com> - train-3
- Added module_hotfixes=1 as needed for CentOS 8

* Fri Apr 03 2020 Alfredo Moralejo <amoralej@redhat.com> - train-2
- Added repos for CentOS 8

* Tue Oct 15 2019 Yatin Karel <ykarel AT redhat.com> - train-1
- first stable release and general availability of RDO Train

* Mon Oct 07 2019 Alfredo Moralejo <amoralej AT redhat.com> - train-0.1
- Fix build which contained wrong repo files.

* Mon Oct 07 2019 Alfredo Moralejo <amoralej AT redhat.com> - train-0
- Pre-release RDO Train repo setup for bootstraping Train CI

* Thu Sep 19 2019 Alfredo Moralejo <amoralej@redhat.com> - stein-3
- Move VirtSIG repo to mirrorlist

* Wed May 22 2019 Arun S A G <sagarun AT gmail.com> - stein-2
- Fix breakage in RHEL

* Tue Apr 30 2019 Alfredo Moralejo <amoralej AT redhat.com> - stein-1
- first stable release and general availability of RDO Stein

* Thu Mar 28 2019 Alfredo Moralejo <amoralej AT redhat.com> - stein-0
- Pre-release RDO Stein repo setup for bootstraping Stein CI

* Fri Aug 31 2018 Yatin Karel <ykarel AT redhat.com> - rocky-1
- First stable release and general availability of RDO Rocky

* Thu Aug 16 2018 Alfredo Moralejo <amoralej AT redhat.com> - rocky-0
- Pre-release RDO Rocky repo setup for bootstraping Rocky CI

* Wed Feb 28 2018 Alfredo Moralejo <amoralej AT redhat.com> - queens-1
- First stable release and general availability of RDO Queens

* Thu Feb 22 2018 Alfredo Moralejo <amoralej AT redhat.com> - queens-0
- Pre-release RDO Queens repo setup for bootstraping Queens CI

* Wed Aug 30 2017 David Moreau Simard <dmsimard AT redhat.com> - pike-1
- First stable release and general availability of RDO Pike

* Fri Aug 25 2017 Alan Pevec <apevec AT redhat.com> - pike-0
- Pre-release RDO Pike repo setup for bootstraping Pike CI

* Mon May 8 2017 David Moreau Simard <dmsimard AT redhat.com> - ocata-3
- Move the location for the rdo-trunk-ocata-tested repository

* Wed Feb 22 2017 David Moreau Simard <dmsimard AT redhat.com> - ocata-2
- First stable release and general availability of RDO Ocata

* Fri Feb 17 2017 David Moreau Simard <dmsimard AT redhat.com> - ocata-1
- The -testing repository is now self contained: disable the trunk-tested
  repository by default.
- Change the URL of the tested repository to point to ocata rather than master

* Wed Nov 9 2016 David Moreau Simard <dmsimard AT redhat.com> - ocata-0
- First version of the Ocata release RPM
- No OpenStack stable repositories are available for Ocata:
  Only trunk-tested and testing repositories are enabled by default
