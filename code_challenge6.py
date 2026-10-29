s = int(input("Enter a number: "))
a = 0
for x in range (5):
    if a != s:
        for y in range (x+1):
            if a != s:
                a+=1
                print(a, end = " ")
            elif a==s:
                print ("",end="")
        print()
