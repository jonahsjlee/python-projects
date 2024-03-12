'''
Name: Jonah Lee
Computing ID: wkx9ff
'''
#global card_list
#card_list = {"2":2, "3":3, "4":4, "5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":1}

def card_to_value(card):
    card_list = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10,"A": 1}
    for value in card_list:
        if value == card:
            return card_list[value]

def hard_score(hand):
    total = 0
    for card in hand[0:len(hand)]:
        total += card_to_value(card)
    return total

def soft_score(hand):
    first_ace = True
    total = 0
    for card in hand[0:len(hand)]:
        if card == "A" and first_ace == True:
            total += 11
            first_ace = False
        else:
            total += card_to_value(card)
    return total

