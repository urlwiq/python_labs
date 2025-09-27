price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(F'База после скидки:{'%.2f'%base}')
print(F'НДС:{'%.2f'%vat_amount}')
print(F'Итого к оплате:{'%.2f'%total}')
