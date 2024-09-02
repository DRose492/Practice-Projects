# A script for encrypting and decripting messaging using the Playfair Cipher


# The following variables are global variables
Text = ""       # Grabs thephrase to be encrypted/decrypted
Keyword = ""    # The Keyword/phrase to be used to create the grid
i = 0           # A variable used in multiple functions for interation count
Inquiry = ""    # Non-important user inquiry
Encrypt = False
Decrypt = False


# Inquire what the user is trying to do (Encrypt or Decrypt)
while True:
    Inquiry = input("Are you looking to encrypt or decrypt a message? ")
    Inquiry = Inquiry.lower().split()

    for word in Inquiry:
        if word == "encrypt":
            Encrypt = True
            break
        elif word == "decrypt":
            Decrypt = True
            break
    else:
        print("I'm sorry. I didn't catch that. Please try again. \n")
        continue

    break


# Let's get the grid built for either the encription or decryption
Keyword = input("What keyword or keyphrase are we using? ")

def Grid(Keyword):
    Keyword = Keyword.upper().replace("J", "I")
    Seen = set()
    Grid_Temp= []

    for char in Keyword:
        if char not in Seen and char.isalpha():
            Seen.add(char)
            Grid_Temp.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in Seen:
            Seen.add(char)
            Grid_Temp.append(char)

    Rows = [Grid_Temp[i:i+5] for i in range (0, 25, 5)]

    return Rows

Grid = Grid(Keyword)


# Retrieve and format the text to be encrypted/decrypted
Text = input("\n What text do you want to encrypt/decrypt? ")

def Input_Format(Text):
    Text = Text.upper().replace("J","I").replace(" ","")
    Pairs = []
    i = 0

    while i < len(Text):
        a = Text[i]
        if (i + 1) < len(Text):
            b = Text[i + 1]
            if a == b:
                Pairs.append((a, "Z"))
                i += 1
            else:
                Pairs.append((a, b))
                i += 2
        else:
            Pairs.append((a, "Z"))
            i += 1

    return Pairs

Pairs = Input_Format(Text)


# Now to define the function to find positions on the grid
def Position(Grid):
    Position_dict = {}
    for row in range(5):
        for col in range(5):
            Position_dict[Grid[row][col]] = (row, col)

    return Position_dict

# Now to encrypt or decrypt the pairs of characters
def Encrypt_Decrypt(Pairs, Grid):
    Position_dict = Position(Grid)
    Encrypted_Text = ""

    for a, b in Pairs:
        Row1, Col1 = Position_dict[a]
        Row2, Col2 = Position_dict[b]

    if Row1 == Row2:                                    # Rule 1 of the Playfair Cipher, if the two letters are located in the same row
        Encrypted_Text += Grid[Row1][(Col1 + 1) % 5]    # Shift both letters over one position to the right, wrapping around as needed.
        Encrypted_Text += Grid[Row2][(Col2 + 1) % 5]
    elif Col1 == Col2:                                  # Rule 2 of the Cipher, if the two letters are located in the same column
        Encrypted_Text += Grid[(Row1 + 1) % 5][Col1]    # Shift both letters down one position, wrapping around as needed.
        Encrypted_Text += Grid[(Row2 + 1) % 5][Col2]
    else:                                               # Rule 3 of the Cipher, if both letters are two corners of a rectangle
        Encrypted_Text += Grid[Row1][Col2]              # Replace that letter with the opposite corner within that same row.
        Encrypted_Text += Grid[Row2][Col1]

    return Encrypted_Text
