from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pretty_date/__init__.py
from pretty_date import __version__ as version

setup(
	name="pretty_date",
	version=version,
	description="change pretty date add datetime in loge",
	author="Amr Basha",
	author_email="amrbasha9000@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
