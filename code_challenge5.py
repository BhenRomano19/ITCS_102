a = int(input("Enter a number: "))
for x in range (a):
    for y in range (a):
        if x + y == a-1 or x == y:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()