n = int(input())
k = list(map(int,input().split()))
k.sort()
print(k[0], k[n-1])