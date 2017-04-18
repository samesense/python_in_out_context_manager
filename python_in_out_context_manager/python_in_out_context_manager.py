# -*- coding: utf-8 -*-
from contextlib import contextmanager

@contextmanager
def in_out(in_file, out_file):
    with open(in_file) as f, open(out_file, 'w') as fout:
        yield f, fout

