# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from python_library import __version__


setup(
    name = "python_library",
    version = __version__,
    description = "A very basic Python library project code base.",
    maintainer = "Atomist",
    packages = ["python_library"],
    platforms = ["any"]
)
