print("This is a HUNGMAN Game")

word_list = ["avatar","babylon","cycolops"]
# word_listss = len(word_list)

import random
chosen_word = random.choice(word_list)

lives = 5

beta = alpha = len(chosen_word)
list_a =[]
# list_a = list_a[alpha]

for letter in chosen_word:
     list_a += "_"
     
print (list_a)

end_game = False

while not end_game:

     for position in range(alpha) :
          user_word = input("geuss a word:\t").lower()

          for position in range(alpha) :

               letter = chosen_word[position]

               if user_word == letter:
                    list_a[position] = letter  

          print(list_a)
          if user_word not in letter :
               print (f'u have',lives,'life remaining')   
               lives = lives - 1    
     if '_'  not in list_a :
          end_game = True
          print("end of the game")