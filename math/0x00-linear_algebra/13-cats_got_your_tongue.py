#!/usr/bin/env python3

import numpy as np


def np_cat(mat1, mat2, axis=0):
    mat = np.concatenate ([mat1, mat2], axis)
    return mat
