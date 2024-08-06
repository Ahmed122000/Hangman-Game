""""
there are some asuumptio in the game: 
1- player 1 is allowed to enter only small letters(no numbers)(sings like , or / etc. won't be hidden)
2- all letters shold be small letters
3- player 2 has only 10 time to mistake or he will lose and will be hanged out
4- it's allowed to enter only 1 character each turn"""

""" for better view for the drawings its better to open a full screen terminal"""

from os import system, name 
from time import sleep 

#function to clear the screen of the output
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
         _ = system('clear')


def print_shapes(x):
    if x == 100:
        print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |       
    |      
    |       
    |      
    |   
   _|____________
    """)
    elif x == 90:
        print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |     
    |       
    |             
    |   
   _|____________
    """)
    elif x == 80:
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |     
    |       
    |     
    |              
   _|____________
    """)
    elif x == 70:
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |       |
    |       
    |         
    |        
   _|____________
    """)
    elif x == 60:
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |       |
    |
    |         
    |        
   _|____________
    """)
    elif x == 50:
        print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|
    |       
    |         
    |        
   _|____________
    """)
    elif x == 40:
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|
    |       
    |
    |
    |      
   _|____________
    """)
    elif x == 30:
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|/
    |
    |     
    |        
   _|____________
    """)
    elif x == 20 :
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|/
    |       |
    | 
    |        
   _|____________
    """)

    elif x == 10 :
         print(""" 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|/
    |       |
    |      /  
    |        
   _|____________
    """)
#----------------------------------------------------------------------------------------------------------------------------------------


score = 100 # score of the player (when it reach 0 the player loses).

#get input from 1st player and check it doesn't contains any digit.
film_name = input("Player 1: please enter the word: ")
while(any(map(str.isdigit, film_name))):
    film_name = input(" Numbers is not allowed.\n please enter any other word without digits: ")

film_name = film_name.lower() #turn the word to lowercase in case the user entered any upercase

#make a list of character of * and spaces for the hidden word
guess =[] 
available_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in film_name:
    if not i.isalnum():
        guess.append(i)
    else:
        guess.append("*")

clear()

# player 2 turn to guess the word
while(score != 0):
    clear() # clear the screen before any gussing to remove the input of the first player

    print_shapes(score) # the beginning shape for the game
    guess = "".join(guess) # turn guess from a list to a normal string
    
    if guess == film_name: # before any gussing check if the player enterd the whole word the last turn or not
        break

    print(f"\n\t\t{guess} \t\t\t score = {score}\n\n") #print the details of the score and last updates of gussing
    print(f"{available_character}\n\n\n")

    #get only one character from 2nd player and check it is not more thatn 1 char
    character = input("player 2: guess any character: ")
    if len(character) != 1:
        print("you're allowed to enter only one char each time, enter again")
        sleep(0.75)
        continue;

    # adding the same letter more and more should not affect the game
    if character not in available_character:
        continue
    
    # check if player 2 gussing is correct or not and remove it from the available letters in both cases
    if character in film_name:
        #add the letter in its place in gussing area on the screen
        index = enumerate(film_name)
        for i ,j in index:
            if j == character:
                guess = list(guess)
                guess[i] = character
            else:
                continue
    else:
        score -= 10 # each wrong answer take 10 points from the score
    available_character.remove(character) #remove used character from available list  


  #end of the game  
clear()
if(guess == film_name):

    print(""" winner \n 
    (_)
    \|/
     |
    / \\
    
    """)
else:
    print("""
    Loser 
     ____________
    |/      |
    |       |
    |       |
    |       |
    |      (_) 
    |      \|/
    |       |
    |      / \\ 
    |        
   _|____________
    
    Game Over
    """)

