# 

name = input("Enter your name ==>")
age = int(input("Enter your age ==>"))

if age >= 60 and age <= 150:
      print ("senior")
elif age >= 49 and age <= 59:
      print("advance adult")
elif age >= 30 and  age >= 48:
      print("adult")
elif age >= 20 and age <=29:
      print("early adulthood")
elif age >= 13 and age <= 19:
      print("teeneger")
elif age >= 6 and age <= 12:
      print("kid")
elif age >= 1 and age <= 5:
      print("infant")
else: 
      print("INVALID")