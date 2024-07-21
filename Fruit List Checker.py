Fruit = ["Apple", "Cherry", "Grape", "Orange"]

X = input("Enter a fruit ")

if Fruit.count(X) is True:
    print("That fruit is in here.")
else:
    print("That fruit is not in here.")
    Y = input("Would you like to add it? Yes or No? ")
    if Y.upper() == "YES":
        Fruit.append(X)
        print("Fruit added to the list.")
    else:
        print("Ok then.")
