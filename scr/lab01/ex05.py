snp= input('ФИО:').split()
init = [i[0] for i in snp]
print(F'Инициалы: {''.join(init)}.')
print(F'Длина (символов): {len(''.join(snp))}')