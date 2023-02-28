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
sys.path.insert(0, os.path.abspath('..'))


# Location of additional Python modules for Sphinx (like Sphinx extensions, Need definitions etc.)
# For adding additional input file paths, see "include_patterns" below

project = 'Demo Project'
copyright = '2022'
author = 'Demo Demo'

print("\n\nHallo\n\n")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
              'sphinx_needs'
              #'sphinx.ext.autodoc',
              #'sphinx.ext.napoleon',
              #'sphinx.ext.viewcode',
              #'breathe',
              #'sphinx_cpp_autodoc',
              #'sphinx_cpp_autodoc.napoleon',
              #'sphinx_cpp_autodoc.viewcode',
      ]



exclude_patterns = []

needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
               # Kept for backwards compatibility
               dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node")
           ]



#Regular Expression a needs ID (automatic or manual) needs to fulfill
needs_id_regex = '^[a-zA-Z0-9_]{5,}'



def setup(app):
    print("\n\nHallo2\n\n")