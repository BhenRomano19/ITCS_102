s = int(input("Enter a number: "))
a = 1
for x in range (5):
    for y in range (x+1):
        print(a, end = " ")
        a += 1
    print()