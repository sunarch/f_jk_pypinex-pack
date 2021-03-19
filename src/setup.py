################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
	],
	description = "Supports various ways of compressing/uncompressing files: gzip, bzip2, xz, tar and uploadpack.",
	include_package_data = True,
	install_requires = [
		"pypine",
	],
	keywords = [
		"pypine",
		"pypinex",
		"gzip",
		"bzip2",
		"xz",
		"uploadpack",
		"tar",
	],
	license = "Apache2",
	name = "pypinex_pack",
	package_data = {
		"": [
			"pypinex_info.json",
		],
	},
	packages = [
		"pypinex_pack",
	],
	version = "0.2021.3.19",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
