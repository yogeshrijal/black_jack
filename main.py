import random
import sys
from art import  logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = ['Y', 'N']

def your_cards():
    hand = []
    for _ in range(2):
        card = random.choice(cards)
        hand.append(card)
    return hand

def sum_user(hand):
    score = sum(hand)
    return score

def another(hand):
    card = random.choice(cards)
    hand.append(card)
    return hand

def computer_cards():
    handy = []
    card = random.choice(cards)
    print(f"Computer 1st card: {card}")
    handy.append(card)
    return handy

def sum_computer(handy):
    com_score = sum(handy)
    return com_score

def drew_card(handy):
    while sum_computer(handy) < 17:
        handy = another(handy)
    return handy

while True:
    play_game = str(input("Do you want to play a game (Y/N): ").upper())
    if play_game not in start:
        print("Invalid input")
    if play_game == 'N':
        print("Exiting the game")
        sys.exit()
    if play_game == 'Y':
        user_hand = your_cards()
        score = sum_user(user_hand)
        print(f"Your cards: {user_hand} Current score: {score}")
        computer_hand = computer_cards()
        computer_score = sum_computer(computer_hand)

    while True:
        another_card = str(input("Press Y to get another card or press N to pass: ").upper())
        if another_card == 'N':
            print("You passed")
            break

        if another_card == 'Y':
            user_hand = another(user_hand)
            score = sum(user_hand)
            print(f"Your cards: {user_hand}  Current score: {score}")
            if score > 21:
                print("You lose! Over 21.")
                break

    computer_final_card = drew_card(computer_hand)
    computer_final_score = sum_computer(computer_final_card)
    print(f"Computer's cards: {computer_final_card} Score: {computer_final_score}")

    if computer_final_score > 21:
        print("You win! Computer busts.")
    elif score > 21:
        print("You lose! Over 21.")
    elif score == computer_final_score:
        print("Oh! It's a draw.")
    elif score > computer_final_score:
        print("You win!")
    else:
        print("You lose!")
