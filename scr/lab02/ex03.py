def flatten(mat: list[list | tuple]):
    transform_list = []
    for i in mat:
        if not isinstance(i,(list,tuple)):
            raise TypeError('TypeError')
        transform_list.extend(i)
    return transform_list
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))