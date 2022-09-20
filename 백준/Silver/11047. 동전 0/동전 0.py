n, amount = map(int, input().split())
value = []
cnt = 0
count = 0
for _ in range(n):
    value.append(int(input()))
    value.sort(reverse =True)
for i in value:
    if amount >= i:
        count = amount // i
        amount = amount % i
        cnt += count

print(cnt)
