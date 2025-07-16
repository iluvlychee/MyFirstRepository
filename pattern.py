'''

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j * 2, end=" ")
    print()

f = 1
for i in range(1,6):
    for j in range(1):
        s = str(f)
        for k in s:
            print(k, end=" ")
    f = f * 11
    print()

'''


for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j * 5, end=" ")
    print()
