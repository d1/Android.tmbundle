# -*- coding: utf-8 -*-
"""
    jinja2.defaults
    ~~~~~~~~~~~~~~~

    Jinja default filters and tags.

    :copyright: (c) 2009 by the Jinja Team.
    :license: BSD, see LICENSE for more details.
"""
from jinjalib.utils import generate_lorem_ipsum, Cycler, Joiner


# defaults for the parser / lexer
BLOCK_START_STRING = '{%'
BLOCK_END_STRING = '%}'
VARIABLE_START_STRING = '{{'
VARIABLE_END_STRING = '}}'
COMMENT_START_STRING = '{#'
COMMENT_END_STRING = '#}'
LINE_STATEMENT_PREFIX = None
LINE_COMMENT_PREFIX = None
TRIM_BLOCKS = False
NEWLINE_SEQUENCE = '\n'


try:
    range_func = xrange
except NameError:
    range_func = range


# default filters, tests and namespace
from jinjalib.filters import FILTERS as DEFAULT_FILTERS
from jinjalib.tests import TESTS as DEFAULT_TESTS
DEFAULT_NAMESPACE = {
    'range':        range_func,
    'dict':         lambda **kw: kw,
    'lipsum':       generate_lorem_ipsum,
    'cycler':       Cycler,
    'joiner':       Joiner
}


# export all constants
__all__ = tuple(x for x in locals().keys() if x.isupper())