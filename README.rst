Release RPM Update process
==========================

* Do CBS rpmbuild http://cbs.centos.org/koji/packageinfo?packageID=3212
* Copy to repos.fedorapeople.org:repos/openstack and there
  * Update openstack-$release/.htaccess
  * On major release, update the base .htaccess file for rdo-release.rpm

NB starting with Liberty, RDO is distributed using CentOS CloudSIG repository
and signed with CloudSIG key.
http://rdoproject.org/repos/openstack-liberty/ contains only rdo-release-liberty.rpm
