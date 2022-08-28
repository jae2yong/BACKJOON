N, K = map(int,input().split())
L = list(map(int,input().split()))
L_new = sorted(L,reverse=True)
print(L_new[K-1])
