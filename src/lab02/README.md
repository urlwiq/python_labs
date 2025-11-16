## Лабораторная работа 2
### Коллекции и матрицы (list/tuple/set/dict)
### Задание A 
Функция 1 - минимум/максимум
```
def min_max(nums: list[float | int]):
    if len(nums)== 0:
        raise TypeError ('ValueError')
    min_num = min(nums)
    max_num = max(nums)
    return (min_num, max_num)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))
```
![im01.png](/images/lab02/im01.png)

Функция 2 - отсортированный список
```
def unique_sorted(nums: list[float | int]):
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
```

![im02.png](/images/lab02/im02.png)

Функция 3 - расплющенный список списков
```
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
```

![im03.png](/images/lab02/im03.png)

### Задание B 
Функция 1 - транспонирование матриц
```
def transpose(mat: list[list[float | int]]):
    if not isinstance(mat,list):
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
print(transpose([[1],[2], [3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3]]))
print(transpose([[]]))
```

![im04.png](/images/lab02/im04.png)

Функция 2 - Сумма по каждой строке
```
def row_sums(mat: list[list[float | int]]):
    if len(mat) == 0:
        return []
    for i in mat:
        if len(i) != len(mat[0]:
            raise TypeError("ValueError")
    if not isinstance(mat, list):
        raise TypeError('TypeError')
    a = []
    for i in mat:
        sm = 0
        for j in i:
            sm += j
        a.append(sm)
    return a
print(row_sums([[1,2,3], [4,5,6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1,2], [3]]))
```

![im05.png](/images/lab02/im05.png)

Функция 3 - сумма по каждому столбцу
```
def col_sums(mat: list[list[float | int]]):
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
```

![im06.png](/images/lab02/im06.png)