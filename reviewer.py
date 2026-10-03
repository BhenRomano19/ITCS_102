# reviewer for the exam 

age = int(input("ENTER YOUR AGE ==>"))
montly_r = float(input("ENTER YOUR MONTLY REVENUE ==>"))
cs = int(input("ENTER YOUR CREDIT SCORE ==>"))
yrs_in_business = float(input("ENETER YOUR YEARS ON BUSINESS ==> "))
has_defaults = bool(input("DO YOU HAVE A DEFAULT IN YOUR BUSINESS ==>"))
cl_name = input("NAME OF THE COLLATERAL ==>")
cl_value = float(input("ENTER THE VALUE OF THE COLLATERAL ==>"))

max_loan = 0
base_fee = 0
#INPUTS 
if age >= 21 and yrs_in_business >= 2.0 and has_defaults == False:
    print("valid for loaning")
    if cs >= 720:#tier 1 
        print("Your credit score is high") #revenue
        max_loan = 3 * montly_r
        if montly_r >= 50000:
            print("You have above 50k revenue")
            base_fee = max_loan * 0.015
            print("your base fee is set to",base_fee)
        else:
            base_fee = max_loan * 0.025
            print("your base is set to",base_fee)
        # collateral
        if cl_value >= max_loan:
           print("collateral",cl_name, "with a value of ", cl_value, "is accepted") 
        else:
           print("rejected, insufficient value for", cl_name)
        # surcharge
        if cl_value % 5000 != 0:
           base_fee += 250
           print("additional charge the base fee is set to ", base_fee)
        else: 
            print("there is no added on the base fee")
    elif 620 <= cs and cs < 720:
       max_loan = 1.5 * montly_r
       if yrs_in_business >= 5.0:
           base_fee = max_loan * 0.02
           print("business greater than 5 years, base fee is set to", base_fee)
       else:
            base_fee = max_loan *0.035
            print("business greater than 5 years, base fee is set to", base_fee)
    elif cs < 620:
        print("credit score is too low ")
else:
    print("invalid")

     


            

   