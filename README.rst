Overview
========

Integration with Infoblox is implemented in two parts: DHCP driver and DNS
driver. All interaction with Infoblox is done using
`ibcli <http://github.com/slchorne/ibcli>`_ tool that should be accessible by
nova-network and nova-manage services.


Requirements
============

* OpenStack Nova (tested with 2012.1, see Notes_)
* `ibcli <http://github.com/slchorne/ibcli>`_ downloaded
* Crypt::SSLeay, XML::Parser and Time::HiRes Perl modules installed
* Infoblox Perl module installed from Infoblox appliance (see Infoblox docs)

Installation
============

Just run ``python setup.py`` or use your favorite Python package manager (like
pip)

Settings
========

* ``instance_dns_manager`` should be set to ``nova_infoblox.InfobloxDNSDriver``
  to let Nova create DNS records in Infoblox
* ``dhcp_driver`` should be set to ``nova_infoblox.InfobloxDHCPDriver`` to let
  Nova create DHCP records in Infoblox
* ``infoblox_cli_command`` should be set to the appropriate full path to
  ``ibcli`` executable, for testing defaults to just ``ibcli``
* ``infoblox_address`` IP address or DNS name of Infoblox appliance
* ``infoblox_username`` and ``infoblox_password`` are credentials to
  authenticate on Infoblox appliance

Notes
=====

* https://review.openstack.org/14518 is required for DHCP driver
* https://review.openstack.org/14560 allows DNS driver to work with VLAN
  network manager
