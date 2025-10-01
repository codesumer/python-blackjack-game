import random

suits = ["Spades","Hearts","Diamonds","Clubs"]
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
rankvalue= {"Ace": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10}





def card():
    return random.choice(ranks), random.choice(suits)

def hand_value(cards):  
    total= sum(rankvalue[r] for r,s in cards)
    aces = sum(1 for r,s in cards if r == "Ace")
    while total > 21 and aces:
        total -= 10  # count Ace as 1 instead of 11
        aces -= 1
    return total


playercards= [card(), card()]
compcards= [card(), card()]

#Player Cards
print("Your Cards:", ', '.join([f"{r} of {s}" for r,s in playercards]))
playervalue= hand_value(playercards)
print(playervalue)

#Dealer Cards
print("Dealer shows:", f"{compcards[0][0]} of {compcards[0][1]}")
compvalue= hand_value(compcards)


while True:
        playervalue= hand_value(playercards)
        compvalue= hand_value(compcards)
        if playervalue>21:
            print("BUST!")
            break
        elif playervalue==21:
            print("BLACKJACK!")
            break
        elif playervalue<21:
            a= str(input("HIT or STAND?:"))
            if a.lower()== "hit":
                playercards.append(card())
                print("Your Cards:", ', '.join([f"{r} of {s}" for r,s in playercards]))
                playervalue = hand_value(playercards)
                print(playervalue)
            else:
                print(f"You stand at: {playervalue}")
                break
                
if playervalue <= 21:
    compvalue = hand_value(compcards)
    while compvalue < 17:
        compcards.append(card())
        compvalue = hand_value(compcards)

    print("Dealer's final hand:", ', '.join([f"{r} of {s}" for r,s in compcards]))
    print("Dealer total:", compvalue)

    # Decide winner
    if compvalue > 21:
        print("Dealer busts! You win!")
    elif compvalue > playervalue:
        print("Dealer wins!")
    elif compvalue < playervalue:
        print("You win!")
    else:
        print("Push! (tie)")

