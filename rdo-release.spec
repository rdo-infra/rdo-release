Name:           rdo-release
Version:        newton
Release:        1
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/redhat-openstack/rdo-release
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
* Tue Aug 23 2016 Haïkel Guémar <hguemar@fedoraproject.org> - newton-1
- Add Virt SIG qemu-kvm-ev repo (RHBZ#1367696)

* Thu Jul 7 2016 Alan Pevec <apevec AT redhat.com> - newton-0
- Add Newton pre-release testing repo

