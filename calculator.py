size = float(0)

while True:

    s = input("Would you like \"l\" or \"xl\" pizza? ").lower()
    while s != "l" and s != "xl":
        print("\nINVALID INPUT")
        s = input("Would you like \"l\" or \"xl\" pizza? ").lower()

    # initialize t out of range just to enter while loop
    t = float(10)
    while t not in range (0,5):
        #print("INVALID INPUT")
        t = input("How many toppings? (0-4) ")
        # check for input that can't be converted to float
        try:
            t = float(t)
        except ValueError:
            continue

    if s.casefold() == "l":
        size = 6
    elif s.casefold() == "xl":
        size = 10
    #if t != 0:
        #size = (round(size+(0.0167*(t**3) - 0.1*(t**2) + 0.9333*t + 0.15), 2))
    #    size = (round((0.0167*(t**3) - 0.1*(t**2) + 0.9333*t + 0.15), 2))
    match t:
        case 1: topping = 1.00
        case 2: topping = 1.75
        case 3: topping = 2.50
        case 4: topping = 3.35
        case _: topping = 0.0
    # update price with toppings
    size = (round(size+topping, 2))
    tax = round(size*0.13, 2)

    print("Subtotal  $" + str(size))
    print("Tax       $" + str(tax))
    print("Total     $" + str(round(float(size + tax), 2)))
    break
