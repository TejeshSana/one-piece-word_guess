from hang_man_stage import *
from word_list import *
import random

print("**********WELCOME TO ONE PIECE HANGMAN WORD GUESS**********")

chosen_word = random.choice(word_list)

lives = 6

display = []

for letter in range(len(chosen_word)):
    display+="_"
end_of_game =  False
while not end_of_game:
    guess = input("Guess a letter 😇 : ").lower()

    if guess in display:
        print(f"You already guessed the word {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if(letter==guess):
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} that is not in the word.You lose a life")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("                         ****************************       ")
            print("YOU LOST YOUR LIFE IN SEARCH OF WORLD's GREATEST TREASURE , ONE PIECE 😵!!! You Lose!!!")
            print("                         ****************************       ")
            print(f"solution is {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("                         ****************************       ")
        print("                  ********YOU FOUND THE ONE PIECE 😊!!!********")
        print("                         ****************************       ")
        print("WEALTH, FAME , POWER. THE MAN WHO HAD ACQUIRED EVERYTHING IN THIS WORLD, THE PIRATE KING")
    print(stages[lives])


