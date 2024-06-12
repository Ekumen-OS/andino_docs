# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Andino'
copyright = '2024, Ekumen'
author = 'ekumenlabs'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinxcontrib.video',
    'sphinx_rtd_theme'
]

templates_path = []

# TODO when all the migration is done, only .rst files will be used as source files
source_suffix = ['.rst', '.md']

master_doc = 'index'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Title of the html page.
html_title = "Andino Documentation"

# Icon of the window.
html_favicon = 'media/real_robot.png'

# Logo of the page. Logo will be put on top of the sidebar.
html_logo = 'media/logo_black.svg'

# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
html_show_sphinx = False

html_theme = 'sphinx_rtd_theme' # Default one is alabaster, you can change it installing other themes (e.g: furo)
html_static_path = ['media', 'other/media', 'package_summary/media']
htmlhelp_basename = 'andino'
