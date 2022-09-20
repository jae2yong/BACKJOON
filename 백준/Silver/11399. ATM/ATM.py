n = int(input())
people = list(map(int, input().split()))
people.sort()
sum = 0
sum2 = 0
for i in people:
    #print(i)
    sum += int(i)
    #print(sum)
    sum2 += sum
print(sum2)