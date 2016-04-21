#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from test.skeleton import fib

__author__ = "Nikhil Kishore"
__copyright__ = "Nikhil Kishore"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
