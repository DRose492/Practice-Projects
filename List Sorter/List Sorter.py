#This code is meant to take in an entered list of entries from the user and sort them in multiple different way according to what the user chooses.


#Lists that will be filled
Order_List = []
Reference_List01 = []
Reference_List02 = []
Sorted_List = []

#Needed variables
Entry = True
Item = ""
Inquiry = ""
Options = ""
Groupings = ""

#While loop to gather the items needed to be sorted
while Entry:
    Item = input("What item are you adding? ")
    while True:
        Inquiry = input("Do you want to add more items? [YES,NO] ")
        Inquiry = Inquiry.upper()
        if Inquiry == "NO":
            Entry = False
            break
        elif Inquiry == "YES":
            break
        else:
            print("Invalid choice. Please try again")
            continue

#Quickly reading the text file with the initial sorting options, as well as a list of sub groups for when sorting by sub groups.
with open("Options.txt") as file:
    Options = file.readlines()
Options = [line.strip() for line in Options]
with open("Themes.txt") as file:
    Themes = file.readlines()
Themes = [line.strip() for line in Themes]

#The main while loop that allows the user to sort the list they created in various fashions.
while True:
    for Item in Options:
        print("\n Options: \n")
        print(f"* {Item}")
    Inquiry = input("\n How would you like the list to be sorted ")
    if Inquiry == "Y":
        print("Good Choice!!!")
    else:
        print("Invalid choice. Please try again")
        continue
