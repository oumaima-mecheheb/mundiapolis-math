#!/usr/bin/env python3

def matrix_shape(matrix):
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])


def add_recursive(mat1, mat2):
    if type(mat1[0]) is not list:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        result = []
        for i in range(len(mat1)):
            inner = add_recursive(mat1[i], mat2[i])
            result.append(inner)
        return result


def add_matrices(mat1, mat2):
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        return add_recursive(mat1, mat2)

add_matrices = __import__('101-the_whole_barn').add_matrices

mat1 = [1, 2, 3]
mat2 = [4, 5, 6]
print(add_matrices(mat1, mat2))
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices(mat1, mat2))
mat1 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
         [[9, 10, 11, 12], [13, 14 ,15, 16]],
         [[17, 18, 19, 20], [21, 22, 23, 24]]],
        [[[25, 26, 27, 28], [29, 30, 31, 32]],
         [[33, 34, 35, 36], [37, 38, 39, 40]],
         [[41, 42, 43, 44], [45, 46, 47, 48]]]]
mat2 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[19, 110, 111, 112], [113, 114 ,115, 116]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[133, 134, 135, 136], [137, 138, 139, 140]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
mat3 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
         [[117, 118, 119, 120], [121, 122, 123, 124]]],
        [[[125, 126, 127, 128], [129, 130, 131, 132]],
         [[141, 142, 143, 144], [145, 146, 147, 148]]]]
print(add_matrices(mat1, mat2))
print(add_matrices(mat1, mat3))