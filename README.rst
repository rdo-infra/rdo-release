Release RPM Update process
==============

* Do local rpmbuild.
* If ever need release rpm from elsewhere then copy, then
* add git tags, and push changes and tags
* Copy to rdo-stage:openstack-$release/ and there

  * Update openstack-$release/.htaccess
  * Link from openstack-$release/$dist/
    (be careful. Person who does final sync to fpo should own the symlink dest file too)
  * On major release, update the base .htaccess file for rdo-release.rpm

NB starting with Kilo, RDO is distributed using CentOS CloudSIG repository
and signed with CloudSIG key.
http://rdoproject.org/repos/openstack-kilo/ contains only rdo-release-kilo.rpm
