m, n, l = map(int, input().split())
if m==n and n==l and m==l:
  print(10000+m*1000)
elif m==n or n==l:
  print(1000+n*100)
elif m==l:
  print(1000+m*100)
else:
  print(max(m,n,l)*100)