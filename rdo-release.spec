Name:           rdo-release
Version:        train
Release:        2%{dist}
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/rdo-infra/rdo-release
# repository files
Source0001:     rdo-release.repo
Source0002:     rdo-testing.repo
Source0003:     rdo-qemu-ev.repo
Source0004:     messaging.repo
Source0005:     advanced-virtualization.repo
# GPG keys
Source0101:     RPM-GPG-KEY-CentOS-SIG-Cloud
Source0103:     RPM-GPG-KEY-CentOS-SIG-Virtualization-RDO
Source0104:     RPM-GPG-KEY-CentOS-SIG-Messaging

BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -d %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d
%if 0%{?rhel} == 7
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/yum.repos.d
%endif
%if 0%{?rhel} == 8
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/yum.repos.d
%endif

#GPG Keys
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE101} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE103} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE104} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
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
