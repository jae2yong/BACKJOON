k = []
for _ in range(9):
  k.append(int(input()))
#print(k)
k2 = sorted(k)
print(k2[8])
print(k.index(int(k2[8]))+1)
