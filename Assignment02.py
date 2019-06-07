import random
import time

class Card:
    def __init__(self, name, rating, strength, mystique, skill):
        self.name = name
        self.rating = rating
        self.strength = strength
        self.mystique = mystique
        self.skill = skill
        
cards = []
cards.append(Card("Hulk", 9.1, 50, 20, 2)) 
cards.append(Card("Thor", 9.5, 35, 75, 3))
cards.append(Card("Iron Man", 10, 30, 25, 9))
cards.append(Card("Dr. Strange", 8.5, 15, 80, 7))
cards.append(Card("Ant Man", 7, 10, 30, 9.6))
cards.append(Card("Spiderman", 9.8, 25, 50, 9.8))
cards.append(Card("Thanos", 8.1, 45, 60, 5))
cards.append(Card("Captain America", 9.3, 28, 35, 10))
cards.append(Card("Black Panther", 6, 26, 70, 9.5))
cards.append(Card("Groot", 8.3, 48, 65, 1.8))


random.shuffle(cards)

heroDeck = []
systemDeck = []
outdatedDeck = []


while len(cards) > 0:
    heroDeck.append(cards.pop(0))
    systemDeck.append(cards.pop(0))
    

print("WHO's YOUR HERO? MARVEL UNIVERSE TOP TRUMP CARDS GAME: SuperHero1 vs SuperHero2!")
BeginGame = input("Roll Dice? Yes/No: ")
def Roll_Dice():
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    global SuperTurn
    print("SuperHero1 dice no. is: " + str(d1))
    print("SuperHero2 dice no. is: " + str(d2))  
    if d1>d2:
        print("SuperHero1 Avenge!")
        SuperTurn = True
    elif d1<d2:
        print("SuperHero2 Avenge!")
        SuperTurn = False
    else:
        print("TIE. Roll again!")
        Roll_Dice()
    
if BeginGame == "yes":
    Roll_Dice()
elif BeginGame == "no":
    print("Say yes to avenge")
else:
    print("not recognized")
    
   
SuperTurn = True
options = ["1", "2", "3", "4"]
gspellcountp = 0
gspellcountc = 0
rspellcountp = 0
rspellcountc = 0
sh1 = 0
sh2 = 0
rspell = "no"
rspell1 = "no"

while len(heroDeck) > 0 and len(systemDeck) > 0:
    
    time.sleep(1)

    if SuperTurn == True:
        #SuperHero1 resurrect spell
        ra = 0
        if (rspellcountp == 0 and len(outdatedDeck) > 1 and ra == 0):
            rspell = input("SuperHero1, play Resurrect Spell? yes/no: ")
            if (rspell == "yes" and rspellcountp == 0):
                z1 = random.randint(1,len(outdatedDeck))
                heroCard = outdatedDeck.pop(int(z1)-1)
                outdatedDeck.append(heroCard)
                rspellcountp = 1
                ra = 1
            else:
                heroCard = heroDeck.pop(0)
                outdatedDeck.append(heroCard)

        else:
            heroCard = heroDeck.pop(0)
            outdatedDeck.append(heroCard) 

            
        print("SuperHero1 CARD")
        print("Name:", heroCard.name)
        print("1. Rating:", heroCard.rating)
        print("2. Strength:", heroCard.strength)
        print("3. Mystique:", heroCard.mystique)
        print("4. Skill:", heroCard.skill)

        avenge = input("SuperHero1, choose what to avenge? ")
        
        while options.count(avenge) == 0:
            avenge = input("Invalid avenge, try again: ")
        #SuperHero1 god spell
        if (gspellcountp == 0  and len(systemDeck) > 1 and ra == 0):
            gspell = input("SuperHero1, play God Spell? yes/no: ")
            if (gspell == "yes" and gspellcountp == 0):
                gspellcountp = 1
                lec = len(systemDeck)
                print("No of cards in SuperHero2 deck:", lec)
                cardno = input("Card number from SuperHero2 deck? ")
                if (rspellcountc == 0 and len(outdatedDeck) > 1):
                    rspell1 = input("SuperHero2, play Resurrect Spell? yes/no: ")
                    if (rspell1 == "yes" and rspellcountc == 0):
                        z2 = random.randint(1,len(outdatedDeck))
                        mn = outdatedDeck.pop(int(z2)-1)
                        systemDeck.insert(0,mn)
                        choice = input("SuperHero1: 1. Force resurrected card or 2. Force earlier choice ")
                        if (choice == "1"):
                            systemCard = systemDeck.pop(0)
                            outdatedDeck.append(systemCard)
                            rspellcountc = 1
                        else:    
                            systemCard = systemDeck.pop(int(cardno)-1)
                            outdatedDeck.append(systemCard)
                            rspellcountc = 1
                    else:
                        systemCard = systemDeck.pop(int(cardno)-1)
                        outdatedDeck.append(systemCard)
                else:
                    systemCard = systemDeck.pop(int(cardno)-1)
                    outdatedDeck.append(systemCard) 
                    
            else:
                systemCard = systemDeck.pop(0)
                outdatedDeck.append(systemCard) 

        
        else:
            systemCard = systemDeck.pop(0)
            outdatedDeck.append(systemCard) 
        
        print("SuperHero2 CARD")
        print("Name:", systemCard.name)
        print("1. Rating:", systemCard.rating)
        print("2. Strength:", systemCard.strength)
        print("3. Mystique:", systemCard.mystique)
        print("4. Skill:", systemCard.skill)

    else:
        #SuperHero2 resurrect spell
        rb = 0
        if (rspellcountc == 0 and len(outdatedDeck) > 1 and rb == 0):
            rspell1 = input("SuperHero2, play Resurrect Spell? yes/no: ")
            if (rspell1 == "yes" and rspellcountc == 0):
                z2 = random.randint(1,len(outdatedDeck))
                systemCard = outdatedDeck.pop(int(z2)-1)
                outdatedDeck.append(systemCard)
                rspellcountc = 1
                rb = 1
            else:
                systemCard = systemDeck.pop(0)
                outdatedDeck.append(systemCard)

        else:
            systemCard = systemDeck.pop(0)
            outdatedDeck.append(systemCard)
        
       
        print("SuperHero2 CARD")
        print("Name:", systemCard.name)
        print("1. Rating:", systemCard.rating)
        print("2. Strength:", systemCard.strength)
        print("3. Mystique:", systemCard.mystique)
        print("4. Skill:", systemCard.skill)

        
        avenge = input("SuperHero2, choose what to avenge? ")
        print("SuperHero2 chooses", avenge)
        
        #SuperHero2 god spell
        if (gspellcountc == 0 and len(heroDeck) > 1 and rb == 0):
            gspell1 = input("SuperHero2, play God Spell? yes or no: ")
            if (gspell1 == "yes" and gspellcountc == 0):
                gspellcountc = 1
                lep = len(heroDeck)
                print("No of cards in SuperHero1 deck:", lep)
                cardno1 = input("Card number from SuperHero1 deck? ")
                if (rspellcountp == 0 and len(outdatedDeck) > 1):
                    rspell = input("SuperHero1, play Resurrect Spell? yes or no: ")
                    if (rspell == "yes" and rspellcountp == 0):
                        z1 = random.randint(1,len(outdatedDeck))
                        nm = outdatedDeck.pop(int(z1)-1)
                        heroDeck.insert(0,nm)
                        choice1 = input("SuperHero2: 1. Force resurrected card or 2. Force earlier choice ")
                        if (choice1 == "1"):
                            heroCard = heroDeck.pop(0)
                            outdatedDeck.append(heroCard)
                            rspellcountp = 1
                        else:
                            heroCard = heroDeck.pop(int(cardno1)-1)
                            outdatedDeck.append(heroCard)
                            rspellcountp = 1
                    else:
                        heroCard = heroDeck.pop(int(cardno1)-1)
                        outdatedDeck.append(heroCard)
                else:                 
                    heroCard = heroDeck.pop(int(cardno1)-1)
                    outdatedDeck.append(heroCard)
            else:
                heroCard = heroDeck.pop(0)
                outdatedDeck.append(heroCard)

        
        else:
            heroCard = heroDeck.pop(0)
            outdatedDeck.append(heroCard)
                                   
        print("SuperHero1 CARD")
        print("Name:", heroCard.name)
        print("1. Rating:", heroCard.rating)
        print("2. Strength:", heroCard.strength)
        print("3. Mystique:", heroCard.mystique)
        print("4. Skill:", heroCard.skill)

    
    
    SuperHeroWins = False
   
    if avenge == "1":
        SuperHeroWins = (heroCard.rating > systemCard.rating)
    elif avenge == "2":
        SuperHeroWins = (heroCard.strength > systemCard.strength)
    elif avenge == "3":
        SuperHeroWins = (heroCard.mystique > systemCard.mystique)
    elif avenge == "4":
        SuperHeroWins = (heroCard.skill > systemCard.skill)

    time.sleep(1)
    
   
    if SuperHeroWins:
        print("SuperHero1 wins this hand!")
        sh1=sh1+1      
        SuperTurn = True
    else:
        print("SuperHero2 wins this hand!")
        sh2=sh2+1
        SuperTurn = False

time.sleep(2)


if sh1<sh2:
    print("SuperHero2 WINS THE MATCH!")
elif sh1>sh2:
    print("SuperHero1 WINS THE MATCH!")
else:
    print("IT'S A TIE!")
 

time.sleep(2)


print("SuperHero1 total points: ", sh1)
print("SuperHero2 total points: ", sh2)
print("Total cards in Outdated Deck: ", len(outdatedDeck))

time.sleep(2)