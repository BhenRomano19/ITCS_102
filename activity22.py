car_type = ["sports","off road ","van"]
cars = []

while True:
    ans = input("Do you know any car type? (yes or no)")

    if ans.lower() == "yes":
        print("what is this type of car? (select from the list)")
        for x in car_type:
            print(x)

        a_type= input("type ==>")

        cars = input("what type of car is your favorite?")
        car_type.append(cars)
        continue
    else:
        print("Thank you")
        print("so far you have encoded the following")
        for x in cars:
            print(x)
        break

    