#st = float(0)

while True:

    s = input("Would you like Large or Extra Large?").lower()
    while s != "large" and s != "extra large":
        print("\nINVALID INPUT")
        s = input("Would you like Large or Extra Large?").lower()

    t = (input("How many toppings? "))
    t = float(t)
    while t not in range (0,5):
        print("INVALID INPUT")
        t = (input("How many toppings? "))
        t = float()

    if s.casefold() == "large":
        st = 6
    elif s.casefold() == "extra large":
        st = 10
    if t != 0:
        st = (round(st+(0.0167*(t**3) - 0.1*(t**2) + 0.9333*t + 0.15), 2))
    tax = round(st*0.13, 2)

    print("Subtotal      $" + str(st))
    print("Tax      $" + str(tax))
    print("Total     $" + str(round(float(st + tax), 2)))
    break
