from getpass import getpass

acc = False
while acc == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    if username == "romano" and password == "1234":
        print("Access granted")
        acc = True
    else:
        print("Access denied")