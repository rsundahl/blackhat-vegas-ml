# -*- coding: iso-8859-15 -*-

import io
import os
import sys

from nbformat import read, writes

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    print writes(merged)

if __name__ == '__main__':
    notebooks = sys.argv[1:]
    merge_notebooks(notebooks)
