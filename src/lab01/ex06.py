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