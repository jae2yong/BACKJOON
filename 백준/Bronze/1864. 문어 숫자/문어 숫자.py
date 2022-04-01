d = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1 }
while 1:
  n = input()
  if n == '#':
    break
  res = 0
  
  for i in range(len(n)):
    res += d[n[i]] * 8 ** (len(n)-i-1)
  print(res)    