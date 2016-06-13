Name:           rdo-release
Version:        mitaka
Release:        5
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/redhat-openstack/rdo-release
Source0:        rdo-release.repo
Source2:        rdo-testing.repo
Source1:        RPM-GPG-KEY-CentOS-SIG-Cloud


BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -d %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum.repos.d

#GPG Keys
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
* Mon Jun 13 2016 Alan Pevec <apevec AT redhat.com> - mitaka-5
- Add Mitaka Trunk repository

* Mon Apr 11 2016 Alan Pevec <apevec AT redhat.com> - mitaka-2
- Mitaka GA
