print("----------------------------------------------------")
print("Welcome to flow rate to velocity converter, please read the instructions below ")
print("----------------------------------------------------")

ex = True
while ex:
    print("Please select the unit you would like to convert from: ")
    print("1. ml/min")
    print("2. ml/sec")
    print("3. L/min")
    print("4. L/sec")
    print("----------------------------------------------------")
    unit_from = float(input())
    print("----------------------------------------------------")

    while unit_from != 1 and unit_from != 2 and unit_from != 3 and unit_from != 4:
        print("Invalid input, please try again")
        unit_from = float(input())
    multiplier = 1
    if unit_from == 2:
        multiplier = 60
    elif unit_from == 3:
        multiplier = 1000
    elif unit_from == 4:
        multiplier = 60 * 1000

    print("Please input flow rate value: ")
    print("----------------------------------------------------")
    flow_rate = float(input())
    print("----------------------------------------------------")
    while flow_rate < 0:
        print("Invalid input, please try again")
        print("----------------------------------------------------")
        flow_rate = float(input())
        print("----------------------------------------------------")

    print("Please input the diameter of the tube in mm ")
    print("----------------------------------------------------")
    diameter = float(input())
    print("----------------------------------------------------")
    while diameter < 0:
        print("Invalid input, please try again")
        diameter = float(input())
        print("----------------------------------------------------")

    velocity = ((10 * float(flow_rate) * multiplier) / (6 * 3.141592653589793 * ((float(diameter)) ** 2) / 4))

    print("Please select the unit you would like to convert to: ")
    print("1. m/s")
    print("2. cm/s")
    print("----------------------------------------------------")
    unit_to = float(input())
    print("----------------------------------------------------")
    while unit_to != 1 and unit_to != 2:
        print("Please enter a valid option")
        print("Please select the unit you would like to convert to: ")
        print("1. m/s")
        print("2. cm/s")
        print("----------------------------------------------------")
        unit = float(input())
        print("----------------------------------------------------")
    if unit_to == 1:
        print("----------------------------------------------------")
        print("The velocity of the fluid is " + str(velocity / 100) + " m/s")
        print("----------------------------------------------------")
    elif unit_to == 2:
        print("----------------------------------------------------")
        print("The velocity of the fluid is " + str(velocity) + " cm/s")
        print("----------------------------------------------------")

    print("----------------------------------------------------")
    print("")
    print("----------------------------------------------------")

    print("Would you like to convert another value? (y/n)")
    ex = input()
    if ex == "y":
        ex = True
        print("----------------------------------------------------")
        for i in range(3):
            print("|")
        print("----------------------------------------------------")
    else:
        ex = False

print("----------------------------------------------------")
print("----------------------------------------------------")
print("Thank you for using the converter, have a nice day!")
print("----------------------------------------------------")
print("----------------------------------------------------")
