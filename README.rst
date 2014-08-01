Release RPM Update process
==============

* If a major release, generate a new signing key as documented below
* Do local rpmbuild.
* If ever need release rpm from elsewhere then copy, then

  * Sign with appropriate key. Note this will resign. I.E. remove foreman key
    and add our key as only RPM versions prior to 4.1 allowed you to sign a
    package with multiple keys, which causes problems for automatic verification.
* add git tags, and push changes and tags
* Copy to team:/$openstack-stage/openstack-$release/ and there

  * Update openstack-$release/.htaccess
  * sign-rpms rdo-$release rdo-release-$release.*.rpm
  * Link from openstack-$release/$dist/
    (be careful. Person who does final sync to fpo should own the symlink dest file too)
  * On major release, update the base .htaccess file for rdo-release.rpm
  * createrepo ....


New RPM signing key generation
==============================

For each openstack release we regenerate a new key
to reduce long term dependence on older possibly problematic keys

Please ensure your personal key has sufficient trust,
before using it to sign the openstack release key.
Contact P@draigBrady.com for details on this.

Generating a new OpenStack release key (replace "grizzly" with release name)
----------------------------------------------------------------------------
* gpg --gen-key

  * Full RSA/RSA, 4096
  * Expiry: 0
  * Name: rdo-grizzly-sign, email: rdo-info@redhat.com, comment: none
  * pass = select a pass phrase to use here

* Double check passphrase is OK with

  * ``echo "1234" | gpg --no-use-agent -o /dev/null --local-user 'rdo-grizzly-sign' -as - &&
      echo "The correct passphrase was entered for this key"``

* Generate key for rpm

  * ``gpg --export -a 'rdo-grizzly-sign' > RPM-GPG-KEY-RDO-Grizzly``
  * add RPM-GPG-KEY-RDO-Grizzly to the release RPM package

Verify generated key
--------------------
* ``sudo rpm --import RPM-GPG-KEY-RDO-Grizzly``
* ``rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'``


Sign the release (pub not sub) key in the public web of trust
--------------------------------------------------------------
* ``gpg --fingerprint 'rdo-grizzly-sign'``
* ``gpg --sign-key --default-cert-level 3 D97B3247``
* ``gpg --keyserver keys.gnupg.net --send-keys D97B3247``

Make private key available on staging server
-----------------------------------------
* ``gpg --export-secret-key 'rdo-grizzly-sign' > grizzly-team-key``
* ``scp grizzly-team-key team:/$openstack-stage/``
* ``ssh team; cd $openstack-stage``
* ``chmod a-w,o-r grizzly-team-key``
* Each dev does once

  * ``gpg --import grizzly-team-key``

* Each rpm is signed by the team server script, but that essentially does

  * ``rpm --addsign --define "_gpg_name rdo-grizzly-sign" *.rpm``
