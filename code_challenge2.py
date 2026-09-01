#peso denominator

money = int(input(" Money to Deposit ------> "))

libo = money // 1000
libo_sukli = money % 1000
five_hundred = libo_sukli // 500
five_sukli = libo_sukli % 500
two_h = five_sukli // 200
two_h_sukli = five_sukli % 200
one_h = two_h_sukli // 100
one_h_sukli = two_h_sukli % 100
fifte = one_h_sukli // 50
fifte_sukli = one_h_sukli % 50
bente = fifte_sukli // 20
bente_sukli = fifte_sukli % 20
sampo = bente_sukli // 10
sampo_sukli = bente_sukli % 10
lima = sampo_sukli // 5
lima_sukli = sampo_sukli % 5
isa = lima_sukli // 1
isa_sukli = lima_sukli % 1

print("ONE THOUSAND -", libo)
print("FIVE HUNDRED -", five_hundred)
print("TWO HUNDRED -", two_h)
print("ONE HUNDRED -", one_h )
print("FIFTY -", fifte)
print("TWENTY -", bente)
print("TEN -", sampo)
print("FIVE -", lima)
print("ONE -", isa)