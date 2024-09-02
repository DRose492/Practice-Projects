# This script is meant to solve the Displacement formula by gathering neccessary data from users.

# Defining a pesky variable
Initial_Velocity = 0.0

# A while loop to gather the velocity
while True:
    Inquiry = input("Do you know your initial velocity? [YES,NO] ")
    Inquiry = Inquiry.upper()
    if Inquiry == "YES":
        while True:
            Initial_Velocity = input("What is the velocity? [in meters per second] ")
            try:
                Initial_Velocity = float(Initial_Velocity)
                break
            except ValueError:
                print("The value you enter is not a valid measurement. Please try again. \n")
                continue
        break
    elif Inquiry == "NO":
        print("Unfortunately you do not enough data to be able to do this calculation. Please return when you do.")
        exit()
    else:
        print("That is not a valid option. Please try again. \n")
        continue

# A while loop to gather the time if it was not grabbed to calculate the velocity
while True:
    Inquiry = input("Do you know how long you traveled? [YES,NO] ")
    Inquiry = Inquiry.upper()
    if Inquiry == "YES":
        while True:
            Time = input("What is the time in seconds? ")
            try:
                Time = float(Time)
                break
            except ValueError:
                print("The value you enter is not a valid measurement. Please try again. \n")
                continue
        break
    elif Inquiry == "NO":
        print("Unfortunately you do not enough data to be able to do this calculation. Please return when you do.")
        exit()
    else:
        print("That is not a valid option. Please try again. \n")

# A while loop to gather the acceleration
while True:
    Inquiry = input("Do you know your acceleration? [YES,NO] ")
    Inquiry = Inquiry.upper()
    if Inquiry == "YES":
        while True:
            Acceleration = input("What is the acceleration in meters per second squared? ")
            try:
                Acceleration = float(Acceleration)
                break
            except ValueError:
                print("The value you enter is not a valid measurement. Please try again. \n")
                continue
        break
    elif Inquiry == "NO":
        while True:
            Inquiry = input("Ok, that's fine. Do you know the speed that you are going in meters per second? [YES,NO] ")
            Inquiry = Inquiry.upper()
            if Inquiry == "YES":
                while True:
                    Inquiry = input("What is the velocity? ")
                    try:
                        Velocity = float(Inquiry)
                        break
                    except ValueError:
                        print("The value you enter is not a valid measurement. Please try again. \n")
                        continue
                Acceleration = (Velocity - Initial_Velocity) / Time
                print("Awesome!!! For reference, your acceleration was " + str(Acceleration) + " meters per second squared.")
                break
            elif Inquiry == "NO":
                print("Unfortunately you do not enough data to be able to do this calculation. Please return when you do.")
                exit()
            else:
                print("That is not a valid option. Please try again. \n")
                continue
    else:
        print("That is not a valid option. Please try again. \n")

def Displacement():
    Holding_Value01 = float(Initial_Velocity) * float(Time)
    Holding_Value02 = Time * Time
    Holding_Value02 = (Holding_Value02 * Acceleration) / 2
    Result = Holding_Value01 + Holding_Value02
    return Result

Displacement = Displacement()
Displacement = str(Displacement)

print("Given all the data you have provided, your overall displacement is " + Displacement + " meters")
