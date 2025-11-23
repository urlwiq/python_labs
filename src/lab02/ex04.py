def transpose(mat: list[list[float | int]]):
    if not isinstance(mat, list):
        raise TypeError("ValueError")
    if len(mat) == 0:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            raise TypeError("ValueError")
    trans_mat = []
    sr = len(mat)
    st = len(mat[0])
    for i in range(st):
        b = []
        for j in range(sr):
            b.append(mat[j][i])
        trans_mat.append(b)
    return trans_mat


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1, 2], [3]]))
print(transpose([[]]))
