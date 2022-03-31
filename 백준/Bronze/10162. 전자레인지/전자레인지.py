t = int(input())
time = [300, 60, 10]
count = 0
a = []
if t%10 != 0:
    print(-1)
else:
  for i in time:
    if t >= i:
      count = t//i
      t = t%i
      a.append(count)
      
    elif t == 0:
      count = 0
      a.append(count)
    elif t < i:
      i += 1
      a.append(0)
string = ' '.join(map(str, a))
print(string)