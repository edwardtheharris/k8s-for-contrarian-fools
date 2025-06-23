"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

author = "Xander Harris <xandertheharris@gmail.com>"
autoyaml_root = "."
copyright = "(c) 2025, Xander Harris <xandertheharris@gmail.com> All rights reserved."
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
exclude_patterns = ["_build", ".venv", "Thumbs.db", ".DS_Store"]
extensions = [
    "ablog",
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx_last_updated_by_git",
    "sphinxcontrib.autoyaml",
]
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_logo = "_static/img/k8s-the-hard-way.png"
html_sidebars = {
    "**": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
        "ablog/authors.html",
        "ablog/languages.html",
        "ablog/locations.html",
    ]
}

html_static_path = ["_static"]
html_theme = "press"
# Myst Configuration
# https://myst-parser.readthedocs.io/en/latest/configuration.html#extensions
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
]
myst_links_external_new_tab = True
myst_title_to_header = True
project = "Kubernetes the Hard Way"
release = "0.0.1"
source_suffix = ".md"
templates_path = ["_templates"]
