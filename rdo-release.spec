Name:           rdo-release
Version:        mitaka
Release:        7
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
* Tue Jun 13 2017 Haïkel Guémar <hguemar@fedoraproject.org> - mitaka-7
- Add Virt SIG qemu-kvm-ev repo (RHBZ#1367696)

* Wed Nov 9 2016 David Moreau Simard <dmsimard AT redhat.com> - mitaka-6
- Add the pending repository

* Mon Jun 13 2016 Alan Pevec <apevec AT redhat.com> - mitaka-5
- Add Mitaka Trunk repository

* Mon Apr 11 2016 Alan Pevec <apevec AT redhat.com> - mitaka-2
- Mitaka GA
