from matplotlib.pylab import rint


loan_amt= float(input("Enter the loan amount: "))
years= int(input("Enter the number of years: "))
month = years * 12
principal = loan_amt / month
remainingbalance = loan_amt

print("|\tMonth\t|\tPrincipal\t|\tRemaining Balance\t|\tLoan Interest\t\t|\tMonthly Payment\t\t|")
for x in range (1, month + 1):
    remainingbalance -= principal
    loan_interest = remainingbalance * 0.00256
    monthly_payment = principal + loan_interest
#strimg formating 
    print(f"|   {x}\t\t|\t{round(principal, 2)}\t\t|\t{round(remainingbalance, 2)}\t\t\t|\t {round(loan_interest, 2)}\t\t|\t{round(monthly_payment, 2)}\t\t|")