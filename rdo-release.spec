Name:           rdo-release
Version:        pike
Release:        0
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/rdo-infra/rdo-release
# repository files
Source0001:     rdo-release.repo
Source0002:     rdo-testing.repo
Source0003:     rdo-qemu-ev.repo
# GPG keys
Source0101:     RPM-GPG-KEY-CentOS-SIG-Cloud
Source0103:     RPM-GPG-KEY-CentOS-SIG-Virtualization-RDO

BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -d %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/yum.repos.d

#GPG Keys
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE101} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE103} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
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
