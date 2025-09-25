""""
there are some asuumptio in the game: 
1- player 1 is allowed to enter only small letters(no numbers)(sings like , or / etc. won't be hidden)
2- all letters shold be small letters
3- player 2 has only 10 time to mistake or he will lose and will be hanged out
4- it's allowed to enter only 1 character each turn"""

""" for better view for the drawings its better to open a full screen terminal"""
 
from time import sleep 
from utilities import clear, print_shapes, show_result

#get input from 1st player and check it doesn't contains any digit.
def get_guess_word():
    guess_word = input("Player 1: please enter the word: ")
    
    while(any(map(str.isdigit, guess_word))):
        guess_word = input(" Numbers is not allowed.\n please enter any other word without digits: ")
    
    while(guess_word == ("quit" or "Quit")):
        quit()

    guess_word = guess_word.lower() #turn the word to lowercase in case the user entered any upercase
    
    return guess_word


#make a list of character of * and spaces for the hidden word
def init():
    guess_word = get_guess_word()
    hidden_word =[] 
    for i in guess_word:
        if not i.isalnum():
            hidden_word.append(i)
        else:
            hidden_word.append("*")
    
    return guess_word, hidden_word


def main():
    while(True):
        score = 100 # score of the player (when it reach 0 the player loses).
        available_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        guess_word, hidden_word = init()
        
        # player 2 turn to guess the word
        while(score != 0):
            clear() # clear the screen before any gussing to remove the input of the first player

            print_shapes(score) # the beginning shape for the game
            hidden_word = "".join(hidden_word) # turn guess from a list to a normal string
            
            if hidden_word == guess_word: # before any gussing check if the player enterd the whole word the last turn or not
                break

            print(f"\n\t\t{hidden_word} \t\t\t score = {score}\n\n") #print the details of the score and last updates of gussing
            print(f"{available_character}\n\n\n")

            #get only one character from 2nd player and check it is not more thatn 1 char
            user_input = input("player 2: guess any character: ")
            
            if user_input == ("quit" or "Quit"):
                quit()
            
            if len(user_input) != 1:
                print("you're allowed to enter only one char each time, enter again")
                sleep(0.75)
                continue

            # adding the same letter more and more should not affect the game
            if user_input not in available_character:
                print("this letter was used before, enter again")
                sleep(0.75)
                continue
        
            # check if player 2 gussing is correct or not and remove it from the available letters in both cases
            if user_input in guess_word:
                #add the letter in its place in gussing area on the screen
                index = enumerate(guess_word)
                for i ,j in index:
                    if j == user_input:
                        hidden_word = list(hidden_word)
                        hidden_word[i] = user_input
                    else:
                        continue
            else:
                score -= 10 # each wrong answer take 10 points from the score
            
            available_character.remove(user_input) #remove used character from available list  

        #end of the game  
        clear()
        if(hidden_word == guess_word):
            show_result('winner')
        else:
            show_result("loser")

        sleep(1)
        clear()

main()