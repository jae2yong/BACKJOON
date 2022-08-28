n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
    list_new = sorted(list)
for i in range(n):
     print(list_new[i])