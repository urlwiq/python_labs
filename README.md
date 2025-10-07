# python_labs
## Лабораторная работа 1

### Задание 1 

```
name = input('Имя:' )
age = int(input('Возраст:'))
next_age = age + 1
print(F"Привет, {name}! Через год тебе будет {next_age}")
```

![im01.png](/images/lab01/im01.png)

### Задание 2
```
ch1 = input("a:")
ch2 = input("b:")
if ',' in ch1:
    ch1 = ch1.replace(',','.')
if ',' in ch2:
    ch2 = ch2.replace(',','.')
ch1 = float(ch1)
ch2 = float(ch2)
sumc= ch1 + ch2
avg = sumc/2
print(F'sum = {'%.2f'%sumc}; avg = {'%.2f'%avg}')
```

![im02.png](/images/lab01/im02.png)

### Задание 3
```
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(F'База после скидки:{'%.2f'%base}')
print(F'НДС:{'%.2f'%vat_amount}')
print(F'Итого к оплате:{'%.2f'%total}')
```

![im03.png](/images/lab01/im03.png)
 
 ### Задание 4
 ```
 m = int(input('Минуты:'))
hour = m // 60
minutes = m % 60
print(F'{hour}:{minutes:02d}')
```

![im04.png](/images/lab01/im04.png)

### Задание 5
```
snp= input('ФИО:').split()
init = [i[0] for i in snp]
print(F'Инициалы: {''.join(init)}.')
print(F'Длина (символов): {len(''.join(snp))}')
```

![im05.png](/images/lab01/im05.png)

### Задание 6
```
n = int(input())
ochn = 0 
zaochn = 0
for i in range(n):
    snp = input().split()
    if snp[-1]== 'True':
        ochn +=1
    else:
        zaochn +=1
print(ochn,zaochn)
```

![im06.png](/images/lab01/im06.png)

## Лабораторная работа 2

### Задание 1
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

### Задание 2 
```
def unique_sorted(nums: list[float | int]):
    return sorted(set(nums))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
```

![im02.png](/images/lab02/im02.png)

### Задание 3
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

### Задание 4
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

### Задание 5
```
def row_sums(mat: list[list[float | int]]) -> list[float]:
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

### Задание 6
```
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
```

![im06.png](/images/lab02/im06.png)

