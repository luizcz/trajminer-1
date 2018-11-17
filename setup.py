from setuptools import setup, find_packages
from os import path


NUMPY_MIN_VERSION = '1.15.3'
SKLEARN_MIN_VERSION = '0.19.1'
KERAS_MIN_VERSION = '2.2.4'

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='trajminer',
    version='0.0.1.dev1',
    description='A trajectory mining library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lucaspetry/trajminer',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
    keywords='trajectory mining',
    packages=find_packages(exclude=['contrib', 'doc', 'tests']),
    install_requires=[
        'numpy>={0}'.format(NUMPY_MIN_VERSION),
        'sklearn>={0}'.format(SKLEARN_MIN_VERSION),
        'keras>={0}'.format(KERAS_MIN_VERSION)
    ]
)
