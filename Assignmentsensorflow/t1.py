# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""tensorflow_docs is a package for generating python api-reference docs."""

import subprocess
import sys

from setuptools import find_packages
from setuptools import setup

project_name = 'tensorflow-docs'
version = '0.0.0.dev0'

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'astor',
    'absl-py',
    'jinja2',
    'nbformat',
    # TODO(b/182876485): Protobuf 3.20 results in linker errors on Windows
    # Protobuf 4.0 is binary incompatible with what C++ TF uses.
    # We need ~1 quarter to update properly.
    # See also: https://github.com/tensorflow/tensorflow/issues/53234
    # See also: https://github.com/protocolbuffers/protobuf/issues/9954
    # See also: https://github.com/tensorflow/tensorflow/issues/56077
    # This is a temporary patch for now, to patch previous TF releases.
    'protobuf >= 3.12.0, < 3.20',
    'pyyaml',
]

# Dataclasses is in-built from py >=3.7. This version is a backport for py 3.6.
if (sys.version_info.major, sys.version_info.minor) == (3, 6):
  REQUIRED_PKGS.append('dataclasses')

VIS_REQUIRE = [
    'numpy',
    'PILLOW',
    'webp',
]

# https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords
setup(
    name=project_name,
    version=version,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Google Inc.',
    author_email='packages@tensorflow.org',
    url='http://github.com/tensorflow/docs',
    download_url='https://github.com/tensorflow/docs/tags',
    license='Apache 2.0',
    packages=find_packages('tools'),
    package_dir={'': 'tools'},
    scripts=[],
    install_requires=REQUIRED_PKGS,
    extras_require={'vis': VIS_REQUIRE},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow api reference',
    # Include_package_data is required for setup.py to recognize the MANIFEST.in
    #   https://python-packaging.readthedocs.io/en/latest/non-code-files.html
    include_package_data=True,
)