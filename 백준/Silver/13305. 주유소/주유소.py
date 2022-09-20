city = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
total = 0
c = cost[0]
for i in range(city-1):
  if c > cost[i]:
      c = cost[i]
  total += c * dist[i]
print(total)