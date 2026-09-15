print("====================================================")
age = int(input("What is your age? =====>"))
credit_score = int(input("What is your credit score? =====>"))
is_employed = bool(input("Are you employed? =====>"))
annual_income = float(input("What is your annual income? =====>"))
has_collateral = bool(input("Do you have collateral? =====>"))
base_rate = 0.0
print("====================================================")
if age >= 21 and is_employed == True: # tier 1
    print("You are eligible for a loan.")
    if credit_score >= 750: #tier 2
        if annual_income >= 100000:
            base_rate = 4.5
            print("You are eligible for a lower interest rate of", base_rate, "%")
        else:
            base_rate = 5.0
            print("base interest rate is", base_rate, "%")
    elif 600 <= credit_score < 750: #tier 2
        print("you credit score is less than 750, you are eligible for a loan but at a higher interest rate.")
        if has_collateral == True:
            base_rate = 7.0
            print("You are eligible for a lower interest rate of", base_rate, "%")
        elif annual_income >= 400000:
            base_rate = 9.5
            print("Your base rate is now ", base_rate, "%")

  



