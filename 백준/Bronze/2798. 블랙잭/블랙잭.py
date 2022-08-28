N, M = map(int, input().split())
L = list(map(int,input().split()))

max = 0
result = 0

for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1, N):
      if L[i]+L[j]+L[k] > M:
        continue
      else:
        result = L[i]+L[j]+L[k]
        if max <= result:
            max = result
          
print(max)
        