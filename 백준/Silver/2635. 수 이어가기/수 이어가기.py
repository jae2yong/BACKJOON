n = int(input())
count = 0
list = []
for i in range(n+1):
  result = [n, i]
  j = 0
  while(1):
    a = result[j] - result[j+1]
    if a<0:
      break
    result.append(a)
    if count < len(result):
      count = len(result)
      list = result[:]
    j+= 1
print(count)
for k in list:
  print(k, end=' ')
print()