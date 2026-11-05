attendance = True

while attendance == True:
    b = bool (input("Are you present? (True/False): "))
    if b == True:
        print("You are present")
        continue
    else:
        print("You are absent")
        break