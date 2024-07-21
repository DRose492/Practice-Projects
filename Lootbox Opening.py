#This program seeks to replicate how a lootbox from Overwatch works as well as minor tweaks I would make to them
Characters = ["Tracer", "Reaper", "Junkrat", "D.Va", "Lucio"]
PrizesCommon = ["Voice_Line", "Spray"]
PrizesRare = ['Skins', 'Victory_Poses', "Credits"]
PrizesEpic = ['Skins', 'Emotes', 'Highlight_Intro', 'Credits']
PrizesLegendary = ['Skins', 'Credits']
Rarity = ["Common", "Rare", "Epic", "Legendary"]

Box = []
Earned_Credits = 0
YourCredits = 0
YourStuff = []

# These lists contain each character's individual prizes
TracerSkinsRare = ["TRS01", "TRS02", "TRS03", "TRS04"]
TracerSkinsEpic = ["TES01", "TES02"]
TracerSkinsLegend = ["TLS01", "TLS02", "TLS03", "TLS04"]
TracerVictoryPoses = ["TVP01", "TVP03", "TVP03"]
TracerEmotes = ['TEM01', 'TEM02', 'TEM03', 'TEM04',]
TracerSprays = ['TSP01', 'TSP02', 'TSP03', 'TSP04', 'TSP05', 'TSP06', 'TSP07', 'TSP08', 'TSP09', 'TSP10']
TracerHighlights = ['THL01', 'THL02', 'THL03']
TracerVoiceLines = [ 'TVL01', 'TVL02', 'TVL03', 'TVL04', 'TVL05', 'TVL06', 'TVL07', 'TVL08', 'TVL09', 'TVL10']
ReaperSkinsRare = ['RRS01', 'RRS02', 'RRS03', 'RRS04']
ReaperSkinsEpic = ['RES01', 'RES02']
ReaperSkinsLegend = ['RLS01', 'RLS02', 'RLS03', 'RLS04']
ReaperVictoryPoses = ['RVP01', 'RVP02', 'RVP03']
ReaperEmotes = ['REM02','REM02', 'REM03', 'REM04']
ReaperSprays = ['RSP01', 'RSP02', 'RSP03', 'RSP04', 'RSP05', 'RSP06', 'RSP07', 'RSP08', 'RSP09', 'RSP10']
ReaperHighlights = ['RHL01', 'RHL02', 'RHL03']
ReaperVoicelines = ['RVL01', 'RVL02', 'RVL03', 'RVL04', 'RVL05', 'RVL06', 'RVL07', 'RVL08', 'RVL09', 'RVL10']
JunkratSkinsRare = ["JRS01", "JRS02", "JRS03", "JRS04"]
JunkratSkinsEpic = ["JES01", "JES02"]
JunkratSkinsLegend = ["JLS01", "JLS02", "JLS03", "JLS04"]
JunkratVictoryPoses = ["JVP01", "JVP03", "JVP03"]
JunkratEmotes = ['JEM01', 'JEM02', 'JEM03', 'JEM04',]
JunkratSprays = ['JSP01', 'JSP02', 'JSP03', 'JSP04', 'JSP05', 'JSP06', 'JSP07', 'JSP08', 'JSP09', 'JSP10']
JunkratHighlights = ['JHL01', 'JHL02', 'JHL03']
JunkratVoiceLines = [ 'JVL01', 'JVL02', 'JVL03', 'JVL04', 'JVL05', 'JVL06', 'JVL07', 'JVL08', 'JVL09', 'JVL10']
DVaSkinsRare = ["DRS01", "DRS02", "DRS03", "DRS04"]
DVaSkinsEpic = ["DES01", "DES02"]
DVaSkinsLegend = ["DLS01", "DLS02", "DLS03", "DLS04"]
DVaVictoryPoses = ["DVP01", "DVP03", "DVP03"]
DVaEmotes = ['DEM01', 'DEM02', 'DEM03', 'DEM04',]
DVaSprays = ['DSP01', 'DSP02', 'DSP03', 'DSP04', 'DSP05', 'DSP06', 'DSP07', 'DSP08', 'DSP09', 'DSP10']
DVaHighlights = ['DHL01', 'DHL02', 'DHL03']
DVaVoiceLines = [ 'DVL01', 'DVL02', 'DVL03', 'DVL04', 'DVL05', 'DVL06', 'DVL07', 'DVL08', 'DVL09', 'DVL10']
LucioSkinsRare = ["LRS01", "LRS02", "LRS03", "LRS04"]
LucioSkinsEpic = ["LES01", "LES02"]
LucioSkinsLegend = ["LLS01", "LLS02", "LLS03", "LLS04"]
LucioVictoryPoses = ["LVP01", "LVP03", "LVP03"]
LucioEmotes = ['LEM01', 'LEM02', 'LEM03', 'LEM04',]
LucioSprays = ['LSP01', 'LSP02', 'LSP03', 'LSP04', 'LSP05', 'LSP06', 'LSP07', 'LSP08', 'LSP09', 'LSP10']
LucioHighlights = ['LHL01', 'LHL02', 'LHL03']
LucioVoiceLines = [ 'LVL01', 'LVL02', 'LVL03', 'LVL04', 'LVL05', 'LVL06', 'LVL07', 'LVL08', 'LVL09', 'LVL10']

import random

Lootboxes = input("How many lootboxes do you have? ")

while int(Lootboxes) > 0:
    Earned_Credits = 0
    Box.clear()
    LBP = 4
    while LBP > 0:
# Let's find the rarity of the prize
        W = random.choice(range(1,101))
        if W > 19:
            V = random.choice(range(2))
            if V == 1:
                W = "Rare"
            else:
                W = "Common"
        elif W > 8 and W < 19:
            V = random.choice(range(2))
            if V == 1:
                W = "Epic"
            else:
                W = "Rare"
        elif W > 0 and W < 8:
            V = random.choice(range(2))
            if V == 1:
                W = "Legendary"
            else:
                W = "Epic"
# Time to determine the type of prize
        if W == "Common":
            X = random.choice(PrizesCommon)
        elif W == "Rare":
            X = random.choice(PrizesRare)
        elif W == "Epic":
            X = random.choice(PrizesEpic)
        else:
            X = random.choice(PrizesLegendary)
# Let's knock out the credits part
        if X == "Credits":
            if W == "Rare":
                X = '50 Credits'
                Box.append(X)
                Earned_Credits = Earned_Credits + 50
                LBP = LBP - 1
            elif W == "Epic":
                X = '200 Credits'
                Box.append(X)
                Earned_Credits = Earned_Credits + 200
                LBP = LBP - 1
            else:
                X = '500 Credits'
                Box.append(X)
                Earned_Credits = Earned_Credits + 500
                LBP = LBP - 1
# And now for the skins
        elif X == "Skins":
            Y = random.choice(Characters)
            if Y == "Tracer":
                if W == "Rare":
                    Z = random.choice(TracerSkinsRare)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 15
                        Box.append("A duplicate rare Tracer skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A rare Tracer skin")
                elif W == "Epic":
                    Z = random.choice(TracerSkinsEpic)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 50
                        Box.append("A duplicate epic Tracer skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("An epic Tracer skin")
                else:
                    Z = random.choice(TracerSkinsLegend)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 200
                        Box.append("A duplicate legendary Tracer skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A legendary Tracer skin")
            elif Y == "Reaper":
                if W == "Rare":
                    Z = random.choice(ReaperSkinsRare)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 15
                        Box.append("A duplicate rare Reaper skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A rare Reaper skin")
                elif W == "Epic":
                    Z = random.choice(ReaperSkinsEpic)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 50
                        Box.append("A duplicate epic Reaper skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("An epic Reaper skin")
                else:
                    Z = random.choice(ReaperSkinsLegend)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 200
                        Box.append("A duplicate legendary Reaper skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A legendary Reaper skin")
            elif Y == "Junkrat":
                if W == "Rare":
                    Z = random.choice(JunkratSkinsRare)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 15
                        Box.append("A duplicate rare Junkrat skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A rare Junkrat skin")
                elif W == "Epic":
                    Z = random.choice(JunkratSkinsEpic)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 50
                        Box.append("A duplicate epic Junkrat skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("An epic Junkrat skin")
                else:
                    Z = random.choice(JunkratSkinsLegend)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 200
                        Box.append("A duplicate Junkrat skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A legendary Junkrat skin")
            elif Y == "D.Va":
                if W == "Rare":
                    Z = random.choice(DVaSkinsRare)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 15
                        Box.append("A duplicate rare D.Va skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A rare D.Va skin")
                elif W == "Epic":
                    Z = random.choice(DVaSkinsEpic)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 50
                        Box.append("A duplicate epic D.Va skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("An epic D.Va skin")
                else:
                    Z = random.choice(DVaSkinsLegend)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 200
                        Box.append("A duplicate legendary D.Va skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A legendary D.Va skin")
            else:
                if W == "Rare":
                    Z = random.choice(LucioSkinsRare)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 15
                        Box.append("A duplicate rare Lucio skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A rare Lucio skin")
                elif W == "Epic":
                    Z = random.choice(LucioSkinsEpic)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 50
                        Box.append("A duplicate epic Lucio skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("An epic Lucio skin")
                else:
                    Z = random.choice(LucioSkinsLegend)
                    if YourStuff.count(Z) == True:
                        Earned_Credits = Earned_Credits + 200
                        Box.append("A duplicate legendary Lucio skin")
                    else:
                        YourStuff.append(Z)
                        Box.append("A legendary Lucio skin")
            LBP = LBP - 1
# And now for emotes
        elif X == "Emotes":
            Y = random.choice(Characters)
            if Y == "Tracer":
                Z = random.choice(TracerEmotes)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Tracer emote")
                else:
                    YourStuff.append(Z)
                    Box.append("A Tracer emote")
            elif Y == "Reaper":
                Z = random.choice(ReaperEmotes)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Reaper emote")
                else:
                    YourStuff.append(Z)
                    Box.append("A Reaper emote")
            elif Y == "Junkrat":
                Z = random.choice(JunkratEmotes)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Junkrat emote")
                else:
                    YourStuff.append(Z)
                    Box.append("A Junkrat emote")
            elif Y == "D.Va":
                Z = random.choice(DVaEmotes)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate D.Va emote")
                else:
                    YourStuff.append(Z)
                    Box.append("A D.Va emote")
            else:
                Z = random.choice(LucioEmotes)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Lucio emote")
                else:
                    YourStuff.append(Z)
                    Box.append("A Lucio emote")
            LBP = LBP - 1
# And now the Highlight Intros
        elif X == "Highlight_Intro":
            Y = random.choice(Characters)
            if Y == "Tracer":
                Z = random.choice(TracerHighlights)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Tracer Highlight Intro")
                else:
                    YourStuff.append(Z)
                    Box.append("A Tracer Highlight Intro")
            elif Y == "Reaper":
                Z = random.choice(ReaperHighlights)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Reaper Highlight Intro")
                else:
                    YourStuff.append(Z)
                    Box.append("A Reaper Highlight Intro")
            elif Y == "Junkrat":
                Z = random.choice(JunkratHighlights)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Junkrat Highlight Intro")
                else:
                    YourStuff.append(Z)
                    Box.append("A Junkrat Highlight Intro")
            elif Y == "D.Va":
                Z = random.choice(DVaHighlights)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate D.Va Highlight Intro")
                else:
                    YourStuff.append(Z)
                    Box.append("A D.Va Highlight Intro")
            else:
                Z = random.choice(LucioHighlights)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 50
                    Box.append("A duplicate Lucio Highlight Intro")
                else:
                    YourStuff.append(Z)
                    Box.append("A Lucio Highlight Intro")
            LBP = LBP - 1
#And now the Victory Poses
        elif X == "Victory_Pose":
            Y = random.choice(Characters)
            if Y == "Tracer":
                Z = random.choice(TracerVictoryPoses)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 15
                    Box.append("A duplicate Tracer victory pose")
                else:
                    YourStuff.append(Z)
                    Box.append("A Tracer victory pose")
            elif Y == "Reaper":
                Z = random.choice(ReaperVictoryPoses)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 15
                    Box.append("A duplicate Reaper vicotry pose")
                else:
                    YourStuff.append(Z)
                    Box.append("A Reaper victory pose")
            elif Y == "Junkrat":
                Z = random.choice(JunkratVictoryPoses)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 15
                    Box.append("A duplicate Junkrat vicotry pose")
                else:
                    YourStuff.append(Z)
                    Box.append("A Junkrat victory pose")
            elif Y == "D.Va":
                Z = random.choice(DVaVictoryPoses)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 15
                    Box.append("A duplicate D.Va vicotry pose")
                else:
                    YourStuff.append(Z)
                    Box.append("A D.Va victory pose")
            else:
                Z = random.choice(LucioVictoryPoses)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 15
                    Box.append("A duplicate Lucio vicotry pose")
                else:
                    YourStuff.append(Z)
                    Box.append("A Lucio victory pose")
            LBP = LBP - 1
#And nown the Sprays
        elif X == "Spray":
            Y = random.choice(Characters)
            if Y == "Tracer":
                Z = random.choice(TracerSprays)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Tracer spray")
                else:
                    YourStuff.append(Z)
                    Box.append("A Tracer spray")
            elif Y == "Reaper":
                Z = random.choice(ReaperSprays)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Reaper spray")
                else:
                    YourStuff.append(Z)
                    Box.append("A Reaper spray")
            elif Y == "Junkrat":
                Z = random.choice(JunkratSprays)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Junkrat spray")
                else:
                    YourStuff.append(Z)
                    Box.append("A Junkrat spray")
            elif Y == "D.Va":
                Z = random.choice(DVaSprays)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate D.Va spray")
                else:
                    YourStuff.append(Z)
                    Box.append("A D.Va spray")
            else:
                Z = random.choice(LucioSprays)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Lucio spray")
                else:
                    YourStuff.append(Z)
                    Box.append("A Lucio spray")
            LBP = LBP - 1
# And finally the Voice Lines
        elif X == "Voice_Line":
            Y = random.choice(Characters)
            if Y == "Tracer":
                Z = random.choice(TracerVoiceLines)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Tracer voiceline")
                else:
                    YourStuff.append(Z)
                    Box.append("A Tracer voiceline")
            elif Y == "Reaper":
                Z = random.choice(ReaperVoicelines)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Reaper voiceline")
                else:
                    YourStuff.append(Z)
                    Box.append("A Reaper voiceline")
            elif Y == "Junkrat":
                Z = random.choice(JunkratVoiceLines)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Junkrat voiceline")
                else:
                    YourStuff.append(Z)
                    Box.append("A Junkrat voiceline")
            elif Y == "D.Va":
                Z = random.choice(DVaVoiceLines)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate D.Va voiceline")
                else:
                    YourStuff.append(Z)
                    Box.append("A D.Va voiceline")
            else:
                Z = random.choice(LucioVoiceLines)
                if YourStuff.count(Z) == True:
                    Earned_Credits = Earned_Credits + 5
                    Box.append("A duplicate Lucio voiceline")
                else:
                    YourStuff.append(Z)
                    Box.append("A Lucio voiceline")
            LBP = LBP - 1
# Now time to display the prizes
    print(Box)
    if Earned_Credits > 0:
        print("You earned " + str(Earned_Credits) + " credits in total from this box. Hooray!!!")
        Earned_Credits = Earned_Credits + 50
        print("Plus 50 for opening the box")
        YourCredits = YourCredits + Earned_Credits
        print("Your new total of credits is " + str(YourCredits) + " .")
    else:
        Earned_Credits = Earned_Credits + 50
        YourCredits = YourCredits + Earned_Credits
        print("Plus you also got 50 for opening the box")
        print("Your new total of credits is " + str(YourCredits) + " .")
# And now for some house keeping for the next box, as well as see if there is going to be a next box
    Box.clear
    Lootboxes = int(Lootboxes) - 1
    Continue = input("Do you wanna open another? Y or N ")
    if Continue.upper() == "Y":
        if Lootboxes > 0:
            print("Awesome. Here's the next box.")
        else:
            Continue = "N"
            print("You are all out of loot boxes")
    else:
        print("You have " + str(Lootboxes) + " lootboxes remaining.")
        Lootboxes = 0
        break