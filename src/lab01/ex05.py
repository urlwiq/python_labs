snp = input("ФИО:").split()
init = [i[0] for i in snp]
print(f"Инициалы: {''.join(init)}.")
print(f"Длина (символов): {len(''.join(snp))+2}")
