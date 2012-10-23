import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(name="openstack-nova-infoblox",
      version="0.1",
      description='Infoblox DHCP and DNS drivers for OpenStack Nova',
      long_description=README,
      py_modules=["nova_infoblox"],
      install_requires=[
          "nova",
      ],
)

