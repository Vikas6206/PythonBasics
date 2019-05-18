is_hot = False
is_cold = True

if is_hot:
    print("It's as hot day")
    print("Drink pleanty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm cloths")
else:
    print("Enjoy your day")


price = 1000000
is_goodCredit = False

if is_goodCredit:
    down_payment =0.1 * price;
    print("Put down 10 % of the property")
else:
    down_payment = 0.2 * price;
    print("Put down 10 % of the property")
print(f"Downpoayment is ${down_payment}")