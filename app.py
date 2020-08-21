import os
import csv
import random
import time
from hangman_pictures import hangman, hangman_dead, picture


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def countBack(count, start_message='', end_message=''):
    if count == 0:
        clearScreen()
        return
    clearScreen()
    print(start_message, count, end_message)
    time.sleep(1)
    countBack(count-1, start_message, end_message)


def match(array, word):
    for i in range(len(array)):
        if array[i] != word[i]:
            return False
    return True


def printList(array, text=''):
    for i in array:
        text += i+' '
    print(text)


def play():
    turns = 7
    minimum_length = turns
    words = []
    # Getting Words from csv file
    with open('english_words.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            words.append(row[0])

    word = ""
    guessed = []
    wrong_letters = []

    while len(word) <= minimum_length:
        word = random.choice(words).lower()

    for i in range(len(word)):
        guessed.append('_')

    clearScreen()
    user_name = input("Enter your name: ").strip().title()
    time.sleep(0.2)
    clearScreen()
    print(f"Hi {user_name}!")
    time.sleep(0.5)
    print("Welcome to HANGMAN\n")
    print(picture)
    time.sleep(0.5)
    print("Let's play HANGMAN")
    time.sleep(0.5)

    ready = False
    while not ready:
        cmd = input("Are you ready? (y/n): ")
        if (cmd.lower() == 'y'):
            ready = True
        elif cmd.lower() == 'n':
            quit_answer = input("Are you sure you want to quit? (y/n): ")
            if (quit_answer.lower() == 'y'):
                exit()
        clearScreen()

    countBack(5, start_message="Game is starting in", end_message="seconds.")
    clearScreen()
    win = False
    print(guessed, word)
    while (not match(guessed, word)) and (turns >= 0) and not win:
        clearScreen()
        print(f"Turns: {turns}")
        print(hangman[turns])
        printList(wrong_letters, "Wrong letters: ")
        printList(guessed, "Guessed: ")

        letter = input("Enter the letter or the complete word: ")
        letter = letter.strip().lower()
        if len(letter) > 1:
            if letter == word:
                for i in range(len(word)):
                    guessed[i] = word[i]
            else:
                turns = -1
        elif letter not in wrong_letters and letter not in guessed:
            if (letter in word):
                for i in range(len(word)):
                    if letter == word[i]:
                        guessed[i] = letter
            else:
                turns -= 1
                wrong_letters.append(letter)
        else:
            print(f"The letter {letter} is alredy guessed!")

    if turns < 0:
        clearScreen()
        for i in hangman_dead:
            clearScreen()
            print(i)
            time.sleep(0.1)
    else:
        clearScreen()
        # Won
        print("""
        
            |------------------------|
            | \\    /\\    /  |  |\\  | |
            |  \\  /  \\  /   |  | \\ | |
            |   \\/    \\/    |  |  \\| |
            |------------------------|
        
        """)
        print(picture)

    printList(wrong_letters, "Wrong letters: ")
    printList(guessed, "Guessed: ")
    print("Word: ", word)
    time.sleep(3)

    play_again_answer = input("\nPlay again? (y/n): ")
    if (play_again_answer.lower() == 'y'):
        play()
    else:
        exit()


play()
