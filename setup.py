from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qr_code_app/__init__.py
from qr_code_app import __version__ as version

setup(
	name="qr_code_app",
	version=version,
	description="customization",
	author="ecs",
	author_email="info@erpcloud.systems",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
