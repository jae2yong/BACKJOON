while True:
    a = input()
    if a == "0":
        break
    answer = "no"
    if a == a[::-1]:
        answer = "yes"
    print(answer)

