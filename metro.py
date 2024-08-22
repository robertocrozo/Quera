x = 0

def wwww(b, s):
    global x
    for i in range(8):
        if b[i] == s[7 - i]:
            x += 1

list1 = []
list2 = []

i = 0
while i < 8:
    num = int(input())
    if num == 1 or num == 0:
        list1.append(num)
        i += 1
    else:
        print()

i = 0
while i < 8:
    num = int(input())
    if num == 1 or num == 0:
        list2.append(num)
        i += 1
    else:
        print()

wwww(list1, list2)
print(x)

