#!/usr/bin/env python3

import numpy as np

def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0]):
        return None
    else :
        sum = np.add(mat1, mat2)
    return sum
