# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from shorser import *

def test_none():
    assert jload(jdump(None)) is None

def test_bool():
    assert jload(jdump(True)) is True
    assert jload(jdump(False)) is False

def test_int():
    for i in [0, 1, -1, 38, 12]:
        assert jload(jdump(i)) == i

def test_bytes():
    for s in [b'', b'fafa', b'gre', b'r', b'tjro4']:
        assert jload(jdump(s)) == s

def test_str():
    for s in ['', 'fafa', 'gre', 'r', 'tjro4']:
        assert jload(jdump(s)) == s

def test_object():
    for o in [{}, {'a': 15, 'b': [12, 'x']}]:
        assert jload(jdump(o)) == o
