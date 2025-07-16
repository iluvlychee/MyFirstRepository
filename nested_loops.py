'''
for i in range(10):
    for j in range(3):
        print("innerloop", end = " ")
    print(i)

for i in range(1, 4):
    for j in range(4):
        print(i, end = " ")
    print(i)

for i in range(1, 4):
    for j in range(1,6):
        print(j, end = " ")
    print()

for i in (2, 4, 6, 8, 10):
    for j in range(1,6):
        print(j * 2, end = " ") # * 2 multiplies variable j
    print()

f = 0
for i in range(1, 3):
    for j in range(1,6):
        f = f + 1
        print(f, end = " ")
    print()

for i in range(1,6):
    for j in range(i):
        print(j + 1, end = "")
    print()

for i in range(5, 1, -1):
    for j in range(i + 1):
        print(j, end = " ")
    print()

'''

for j in range(0,11,5):
    print(j, end= " ")
print()