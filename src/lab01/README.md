## Лабораторная работа 1
### Ввод/вывод и форматирование
### Задание 1 - Привет и возраст
```
name = input('Имя:' )
age = int(input('Возраст:'))
next_age = age + 1
print(F"Привет, {name}! Через год тебе будет {next_age}")
```

![im01.png](/images/lab01/im01.png)

### Задание 2 - Сумма и среднее
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

### Задание 3 - Чек: скидка и НДС
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
 
 ### Задание 4 - Минуты → ЧЧ:MM
 ```
 m = int(input('Минуты:'))
hour = m // 60
minutes = m % 60
print(F'{hour}:{minutes:02d}')
```

![im04.png](/images/lab01/im04.png)

### Задание 5 - Инициалы и длина строки
```
snp= input('ФИО:').split()
init = [i[0] for i in snp]
print(F'Инициалы: {''.join(init)}.')
print(F'Длина (символов): {len(''.join(snp))}')
```

![im05.png](/images/lab01/im05.png)

## Задания со звездочкой
### Задание 6 -
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
