#!/usr/bin/env python3
def matrix_shape(matrix):
    type_matrix = type(matrix[0])
    if (type_matrix != list):
        return [len(matrix)]
    else :
        return [len(matrix)] + matrix_shape(matrix[0])
