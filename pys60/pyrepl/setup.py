#   Copyright 2000-2004 Michael Hudson mwh@python.net
#
#                        All Rights Reserved
#
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.
#
# THE AUTHOR MICHAEL HUDSON DISCLAIMS ALL WARRANTIES WITH REGARD TO
# THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
# INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
# RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from distutils.core import setup, Extension

long_desc = """\
pyrepl is a Python library, inspired by readline, for building flexible
command line interfaces, featuring:
 * sane multi-line editing
 * history, with incremental search
 * completion, including displaying of available options
 * a fairly large subset of the readline emacs-mode keybindings
 * a liberal, Python-style, license
 * a new python top-level."""


setup(
    name = "pyrepl",
    version = "0.8.1",
    author = "Michael Hudson",
    author_email = "mwh@python.net",
    url = "http://codespeak.net/pyrepl/",
    license = "MIT X11 style",
    description = "A library for building flexible command line interfaces",
    platforms = ["unix", "linux"],
    packages = ["pyrepl"],
    #ext_modules = [Extension("_pyrepl_utils", ["pyrepl_utilsmodule.c"])],
    scripts = ["pythoni"],
    long_description = long_desc,
    )
