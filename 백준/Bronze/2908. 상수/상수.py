n, m = map(int, input().split())
n_s = str(n)
reverse_n_s =n_s[::-1]
m_s = str(m)
reverse_m_s =m_s[::-1]
if int(reverse_n_s)> int(reverse_m_s) :
  print(reverse_n_s)
else:
  print(reverse_m_s)