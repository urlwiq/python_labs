def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if len(mat) != 0:
        ln = len(mat[0])
    for i in mat:
        if len(i) != ln:
            raise TypeError("ValueError")
    if not isinstance(mat, list):
        raise TypeError("TypeError")
    a = []
    for i in mat:
        sm = 0
        for j in i:
            sm += j
        a.append(sm)
    return a


print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
