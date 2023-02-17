#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

BLACKZSPLOIT_VERSION = "0.1"
BLACKZSPLOIT_DOWNLOAD = ('https://github.com/blackleakz/blackzsploit/tarball/' + BLACKZSPLOIT_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()

def read_requirements():
    with open('requirements.txt') as f:
        return f.readlines()


setup(
	name='blackzsploit',
	packages=[
		'blackzsploit',
		'blackzsploit.ezcolor',
		'blackzsploit.modules',
		'blackzsploit.core',
		'blackzsploit.core.base',
		'blackzsploit.core.utils'],
	package_data={
          'blackzsploit.core': [
              'utils/*',
          ],
      },

	version=BLACKZSPLOIT_VERSION,
	description='blackzsploit is a high level MITM framework',
	long_description=read_file('README.md'),
	long_description_content_type='text/markdown',
    # packages = find_packages(),
    entry_points ={
            'console_scripts': [
                'blackzsploit = blackzsploit.blackzsploit:start_wsf'
            ]
        },

	license='MIT',
	author='Black Leakz',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/blackleakz/blackzsploit',
	download_url=BLACKZSPLOIT_DOWNLOAD,
	keywords=['python3', 'blackzsploit', 'wsf', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)
