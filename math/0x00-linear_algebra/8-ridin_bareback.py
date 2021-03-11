#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    if len(mat2) != len(mat1[0]):
        return None
    else :
        mat = []
        for x in range(len(mat1)):
            rslt = []
            for y in range(len(mat2[0])):
                v = 0
                for z in range(len(mat2)):
                    v += mat1[x][z] * mat2[z][y]
                rslt.append(v)
            mat.append(rslt)
    return mat  
        
mat_mul = __import__('8-ridin_bareback').mat_mul

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))