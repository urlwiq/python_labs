ch1 = input("a:")
ch2 = input("b:")
if "," in ch1:
    ch1 = ch1.replace(",", ".")
if "," in ch2:
    ch2 = ch2.replace(",", ".")
ch1 = float(ch1)
ch2 = float(ch2)
sumc = ch1 + ch2
avg = sumc / 2
print(f"sum = {'%.2f'%sumc}; avg = {'%.2f'%avg}")
