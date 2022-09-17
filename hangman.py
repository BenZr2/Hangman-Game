import os
import math
import random

print("  _   _                                         ")
print(" | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print(" | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print(" |  _  | (_| | | | | (_| | | | | | | (_| | | | |")
print(" |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                    |___/                       ")

word_list = ["apple", "banana", "chameleon", "dolphin", "entropy", "firefighter", "gangmember", "hurricane", "island", "jamaica", "kickoff", "lantern", "mayonaise",
             "narrow", "original", "penalty", "question", "radical", "suncream", "transportation", "universal", "violence", "wonderful", "xylophon", "yourself", "zombies"]

# word = word_list[math.floor(random.randint(0, len(word_list)-1))]
word = random.choice(word_list)
tiles = "_" * len(word)
tries = 5
already_guessed = []


def draw_hangman():
    row1 = "  ____"
    row2 = " |   "
    row3 = " |   "
    row4 = " |  "
    row5 = " |   "
    row6 = " |  "
    row7 = " |   "

    if tries == 4:
        row2 += "|"
    if tries == 3:
        row2 += "|"
        row3 += "O"
    if tries == 2:
        row2 += "|"
        row3 += "O"
        row4 += "/|\\"
    if tries == 1:
        row2 += "|"
        row3 += "O"
        row4 += "/|\\"
        row5 += "|"
    if tries == 0:
        row2 += "|"
        row3 += "O"
        row4 += "/|\\"
        row5 += "|"
        row6 += "/ \\"

    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)


while tries > 0 and "_" in tiles:
    draw_hangman()
    print(tiles)
    guess = input("Guess a letter: ")
    if guess in word and not guess in already_guessed and len(guess) == 1:
        print("Correct")
        for i, letter in enumerate(word):
            # print(i, letter)
            # print(tiles)
            if letter == guess:
                tiles = tiles[:i] + guess + tiles[i+1:]
    else:
        print("False. " + guess.upper() + " is not in the word")
        tries = tries - 1
        print("Tries left: " + str(tries))
    already_guessed.append(guess)
    # os.system('cls')
    print("\n")

draw_hangman()

print("The word was: " + word)

if tries > 0:
    print("You have won")
else:
    print("You have lost")
