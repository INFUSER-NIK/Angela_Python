import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("This is Hungman Game")

#List of words
word_list = ["cosmos","universe","chaos",
             "Space","Stars","Moon","Earthz",
             "Orbit","Solar","Light","Alien",
             "Nova","Nebula","Astoro","Lunar",
             "Planet","Galaxy","Rocket",
             "Meteor","Apollo","Saturn"]

import random
chosen_word = random.choice(word_list).lower()

# Generating a empty list for guessing
display = []

for letter in chosen_word:
    display += "_"
print(display)


word_len = len(chosen_word)

#Enlisting a "life" variable of a game to end at a pace
life = 6
print(f"Your current have life is = {life}")


end_of_game = False

#Starting the Hungman logic
while not end_of_game :
    guess = input("guess a letter : ").lower()
    clear()
    # Checking for the words in the same as guess
    for position in range(word_len):
        letter = chosen_word[position]
        if life >0:
            # print(f"current position : {position}\n current letter : {letter}\n gussed letter : {guess}")
            
            # Right letter gets replace at the correct position
            if letter == guess :
                display[position] = letter

    # Wrong guess deducts life             
    if guess not in chosen_word and life != 1:
        life -= 1 
        print("you have gussed the wrong word pls TRY AGAIN")

        if life == 1 :
            print("you are at your last life GUESS wisly")

        if life == 0 :
            end_of_game = True
            print ("You Lose !!!!!!!!\n",
                   "The word was :",chosen_word)   

            
    if "_" not in display :
        end_of_game = True
        print (" You have won !!")
              
    print(f"You have {life} remaining")
    print(display)