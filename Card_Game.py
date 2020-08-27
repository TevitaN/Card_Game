# Imports:
import time
import random

# Card and suits
Aces = ["AceClubs", "AceSpades", "AceDiamonds", "AceHearts"]
Twos = ["2.Clubs", "2.Spades", "2.Diamonds", "2.Hearts"]
Threes = ["3.Clubs", "3.Spades", "3.Diamonds", "3.Hearts"]
Fours = ["4.Clubs", "4.Spades", "4.Diamonds", "4.Hearts"]
Fives = ["5.Clubs", "5.Spades", "5.Diamonds", "5.Hearts"]
Sixes = ["6.Clubs", "6.Spades", "6.Diamonds", "6.Hearts"]
Sevens = ["7.Clubs", "7.Spades", "7.Diamonds", "7.Hearts"]
Eights = ["8.Clubs", "8.Spades", "8.Diamonds", "8.Hearts"]
Nines = ["9.Clubs", "9.Spades", "9.Diamonds", "9.Hearts"]
Tens = ["10.Clubs", "10.Spades", "10.Diamonds", "10.Hearts"]
Jacks = ["J.Clubs", "J.Spades", "J.Diamonds", "J.Hearts"]
Queens = ["Q.Clubs", "Q.Spades", "Q.Diamonds", "Q.Hearts"]
Kings = ["K.Clubs", "K.Spades", "K.Diamonds", "K.Hearts"]
Deck = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens", "Kings"]

# Player & A.I starting hand
player_hand = []
ai_hand = []

# This function deals five cards to the player hand list.
# It does this by random slection from the Deck list. The result accesses the suits lists and a random selection taken
# from the list stored in the random_picker variable.
def p_shuffle(Deck, player_hand, Aces):
    for i in range(5):
        random_picker = random.choice(Deck)
        #random_picker = "Aces"
        print("Picker", random_picker)
        if random_picker == "Aces":
            Card = random.choice(Aces)
            player_hand.append(Card)
            Aces.remove(Card)

        if random_picker == "Twos":
           Card = random.choice(Twos)
           player_hand.append(Card)
           Twos.remove(Card)

        if random_picker == "Threes":
            Card = random.choice(Threes)
            player_hand.append(Card)
            Threes.remove(Card)

        if random_picker == "Fours":
            Card = random.choice(Fours)
            player_hand.append(Card)
            Fours.remove(Card)

        if random_picker == "Fives":
            Card = random.choice(Fives)
            player_hand.append(Card)
            Fives.remove(Card)

        if random_picker == "Sixes":
            Card = random.choice(Sixes)
            player_hand.append(Card)
            Sixes.remove(Card)

        if random_picker == "Sevens":
            Card = random.choice(Sevens)
            player_hand.append(Card)
            Sevens.remove(Card)

        if random_picker == "Eights":
            Card = random.choice(Eights)
            player_hand.append(Card)
            Eights.remove(Card)

        if random_picker == "Nines":
            Card = random.choice(Nines)
            player_hand.append(Card)
            Nines.remove(Card)

        if random_picker == "Tens":
            Card = random.choice(Tens)
            player_hand.append(Card)
            Tens.remove(Card)

        if random_picker == "Jacks":
            Card = random.choice(Jacks)
            player_hand.append(Card)
            Jacks.remove(Card)
        if random_picker == "Queens":
            Card = random.choice(Queens)
            player_hand.append(Card)
            Queens.remove(Card)

        if random_picker == "Kings":
            Card = random.choice(Kings)
            player_hand.append(Card)
            Kings.remove(Card)
p_shuffle(Deck, player_hand, Aces)
print(player_hand)





