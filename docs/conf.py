# Configuration file for the Sphinx (Needs) documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('.'))


# Location of additional Python modules for Sphinx (like Sphinx extensions, Need definitions etc.)
# For adding additional input file paths, see "include_patterns" below

project = 'Demo Project'
copyright = '2022'
author = 'Demo Demo'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.plantuml',
              'sphinx_needs',
              #'sphinx.ext.autodoc',
              #'sphinx.ext.napoleon',
              #'sphinx.ext.viewcode',
              #'breathe',
              #'sphinx_cpp_autodoc',
              #'sphinx_cpp_autodoc.napoleon',
              #'sphinx_cpp_autodoc.viewcode',
      ]



exclude_patterns = []




#Regular Expression a needs ID (automatic or manual) needs to fulfill
needs_id_regex = '^[a-zA-Z0-9_]{5,}'



