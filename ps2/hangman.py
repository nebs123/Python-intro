# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Loop through secret_word checking that each letter is represented in letters_guessed
    for x in secret_word:
        check = False
        for y in letters_guessed:
            if x == y:
                check = True
                break
        if not check:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #wguessed word to be returned
    word = ""
    
    #loop through secret word and put place holder for letters not in letters_guessed
    for x in secret_word:
        check = False
        
        for y in letters_guessed:
            if x == y:
                check = True
                word += x
                break
        
        if not check:
            word += "_ "
    
    return word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    #string of characters not in letters guessed
    word = ""
    for x in string.ascii_lowercase:
        check = False
        
        for y in letters_guessed:
            
            if x == y:
                check = True
             
                break
        if not check:
            word += x
            
    return word
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #print(secret_word)
    no_of_guesses = 6
    warnings = 3
    guesses = []
    separator = "---------------------"
    print("Welcome to the Hangman game!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have ", warnings, "warnings left")
    print(separator)

    while no_of_guesses > 0 and not is_word_guessed(secret_word,guesses):
        print("You have", no_of_guesses, "guesses left." )
        print("Available letters:", get_available_letters(guesses),end=" " )
        guess = input("Please guess a letter:").lower()
        
        if len(guess) > 1:#Checks if the input is a single  
            print("Please input a single character.")
            print(separator)
            continue
        if not guess.isalpha():#IF guess is not an alphabet character
            print("Oops guess is not a valid letter.",end=" ")
            
            if warnings == 0:#User has no warnings left so subtract guess
                no_of_guesses -= 1
                
            else:
                warnings -= 1
            
            #Print update for the user
            print("You have", warnings, "warnings left:", get_guessed_word(secret_word, guesses) )
        
        else:
            #Need to check if the char is guessed already
            if guess in guesses:
                print("Oops! You've already guessed that letter.",end=" ")
            
                if warnings == 0:
                    no_of_guesses -= 1
                
                else:
                    warnings -= 1
                print("You have", warnings, "warnings left:", get_guessed_word(secret_word, guesses))
            else:
                guesses.append(guess) #Add guess to list if it is a new guess. 
                if guess in secret_word:#If guess in secret
                    print("Good guess:", get_guessed_word(secret_word, guesses))
                
                else: #Guess not in secret word so subtract guesses
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, guesses))
                    
                    if guess in "aeiou":
                        no_of_guesses -= 2
                    else:
                        no_of_guesses -= 1
            
                
        print(separator)
        
    if is_word_guessed(secret_word,guesses):#Game is won
        print("Congratulations, you won!")
        print("Your total score for this game is:", no_of_guesses * unique_chars(secret_word))
    
    else:#Game is lost
        print("Sorry, you ran out of guesses. The word was", secret_word)

def unique_chars(str):
    '''

    Parameters
    ----------
    str : String
        Word whose unique characters are to be counted.

    Returns
    -------
    Int: The number of unique characters in str.

    '''
    
    no_of_unique_chars = 0
    
    for x in string.ascii_lowercase:
        if x in str:
            no_of_unique_chars += 1
    
    return no_of_unique_chars


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")#removes white space 
    
    if len(my_word) != len(other_word):#The words should be of equal length
        return False
    else:
        for x in range(len(my_word)):
            if my_word[x] != "_" and my_word[x] != other_word[x]:
                return False
            
        return True
                
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    match_found = False
    
    for x in wordlist:
        if check_match(my_word, x):
            print(x, end=" ")
            match_found = True

    if not match_found:
        print("No matches found")


def check_match(my_word, other_word):
    '''

    Parameters
    ----------
    my_word : String
        string with _ characters, current guess of secret word .
    other_word : String
        THe word that we are going to check if it is a possible match with my_word making sure 
        the gap matches aren't letters already guessed in the secret worrd

    Returns
    -------
    bool
        return True if other_word is a possible match for my_word and all the letters in other_word that
    correspond to gaps haven't been revealed yet

    '''
    if match_with_gaps(my_word, other_word):
        my_word = my_word.replace(" ", "")#removes white space 
        
        for x in range(len(my_word)):
            if my_word[x] == "_" and other_word[x] in my_word :
                return False
        return True
    else:
        return False


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #print(secret_word)
    no_of_guesses = 6
    warnings = 3
    guesses = []
    separator = "---------------------"
    print("Welcome to the Hangman game!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have ", warnings, "warnings left")
    print(separator)

    while no_of_guesses > 0 and not is_word_guessed(secret_word,guesses):
        print("You have", no_of_guesses, "guesses left." )
        print("Available letters:", get_available_letters(guesses),end=" " )
        guess = input("Please guess a letter:").lower()
        
        if len(guess) > 1:#Checks if the input is a single  
            print("Please input a single character.")
            print(separator)
            continue
        
        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, guesses))
            print("")#Following print statement gets printed on a new line
            print(separator)
            continue
        
        if not guess.isalpha():#IF guess is not an alphabet character
            print("Oops guess is not a valid letter.",end=" ")
            
            if warnings == 0:#User has no warnings left so subtract guess
                no_of_guesses -= 1
                
            else:
                warnings -= 1
            
            #Print update for the user
            print("You have", warnings, "warnings left:", get_guessed_word(secret_word, guesses) )
        
        else:
            #Need to check if the char is guessed already

            
            if guess in guesses:
                print("Oops! You've already guessed that letter.",end=" ")
            
                if warnings == 0:
                    no_of_guesses -= 1
                
                else:
                    warnings -= 1
                print("You have", warnings, "warnings left:", get_guessed_word(secret_word, guesses))
            else:
                guesses.append(guess) #Add guess to list if it is a new guess. 
                if guess in secret_word:#If guess in secret
                    print("Good guess:", get_guessed_word(secret_word, guesses))
                
                else: #Guess not in secret word so subtract guesses
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, guesses))
                    
                    if guess in "aeiou":
                        no_of_guesses -= 2
                    else:
                        no_of_guesses -= 1
            
                
        print(separator)
        
    if is_word_guessed(secret_word,guesses):#Game is won
        print("Congratulations, you won!")
        print("Your total score for this game is:", no_of_guesses * unique_chars(secret_word))
    
    else:#Game is lost
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
