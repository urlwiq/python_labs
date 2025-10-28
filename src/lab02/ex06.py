def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if len(mat) != 0:
        ln = len(mat[0])
    for i in mat:
        if len(i) != ln:
            raise TypeError('"ValueError"')
    if not isinstance(mat, list):
        raise TypeError('TypeError')
    a = []
    for i in range(len(mat[0])):
        b = 0
        for j in range(len(mat)):
            b += mat[j][i]
        a.append(b)
    return a
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))