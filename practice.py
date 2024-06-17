mat1 = [[1,0,0], [0,1,0], [0,0,1]]
mat2 = [[1,2,3], [4,5,6], [7,8,9]]

###
# name: mat_mul
# @param mat1: matrix1
#        mat2: matrix2
#        dim 0 of matrix1 and dim 1 of matrix2 should match.
# @output: 
#        product of mat1 and mat2; None if dimensions doesn't match.
# @example:
#        mat1 = [[1,0,0], [0,1,0], [0,0,1]]
#        mat2 = [[1,2,3], [4,5,6], [7,8,9]]
#        mat1 * mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
###
def mat_mul(mat1, mat2):
    if(len(mat1) != len(mat2[0])):
        return None
    mat = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            tmp_sum = 0
            for k in range(len(mat1)):
                tmp_sum += mat1[i][k]*mat2[k][j]
            mat[i][j] = tmp_sum
    return mat

ans = mat_mul(mat1, mat2);
print(ans);