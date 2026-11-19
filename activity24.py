food = ["burger", "fries", "chiken", "steak", "hatdog", "siopao"  ]
          #0        #1       #2         #3      #4       #5

food_2={"andoy":"burger", "rosario": "fries", "nokma":"chiken", "sarap":"steak", "hat": "hatdog", "pao":"siopao"}

print(food[3])
print(food_2["pao"])

for x,y in food_2.items():
    print("key ==>",x, "values ==>",y)