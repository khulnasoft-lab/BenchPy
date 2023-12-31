# Configuration file for the Sphinx documentation builder.
import os.path as osp
import sys

import benchpy
import benchpy_sphinx_theme

# -- Project information

project = "BenchPy"
copyright = "KhulnaSoft"
author = "Matteo Bettini"
version = benchpy.__version__

# -- General configuration
sys.path.append(osp.join(osp.dirname(benchpy_sphinx_theme.__file__), "extension"))

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "patch",
]

add_module_names = False
autodoc_member_order = "bysource"
toc_object_entries = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "torch": ("https://pytorch.org/docs/master", None),
    "torchrl": ("https://pytorch.org/rl", None),
    "tensordict": ("https://pytorch.org/tensordict", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
html_static_path = [osp.join(osp.dirname(benchpy_sphinx_theme.__file__), "static")]


html_theme = "sphinx_rtd_theme"
html_logo = (
    "https://raw.githubusercontent.com/matteobettini/benchpy_sphinx_theme/master/benchpy"
    "_sphinx_theme/static/img/benchpy_logo.png"
)
html_theme_options = {"logo_only": True, "navigation_depth": 2}
# html_favicon = ('')
html_css_files = [
    "css/mytheme.css",
]

# -- Options for EPUB output
epub_show_urls = "footnote"


def setup(app):
    def rst_jinja_render(app, _, source):
        rst_context = {"benchpy": benchpy}
        source[0] = app.builder.templates.render_string(source[0], rst_context)

    app.connect("source-read", rst_jinja_render)
