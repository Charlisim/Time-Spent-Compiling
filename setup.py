import setuptools

try:
    from setuptools import setup, find_packages
    setuptools_available = True
except ImportError:
    from distutils.core import setup
    setuptools_available = False
# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

params = {}

if setuptools_available:
    params['entry_points'] = {'console_scripts': ['ct = compile_time.__main__:main']}
setuptools.setup(
    name="compile_time",
    version="0.1.0",
    url="https://github.com/Charlisim/Time-Spent-Compiling",

    author="Carlos Simon",
    author_email="csimonts@gmail.com",

    description="Measure time spent compiling",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "click",
        "arrow"
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    **params
)
