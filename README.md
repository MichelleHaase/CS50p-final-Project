# This is Hangman
#### Video Demo:  https://youtu.be/STpkyeZKrng
#### Description:

It's a Hangman game with three levels of difficulty. Imports are sys, to exit after win or loosing conditions are met and wonderwords, which is used to choose a random English word.

the main function only calls each of the other functions after each other.

the function get_level prints the game title once and then prompts the user for an input of 1, 2 or 3 and explains that the Level correlates to the word length and re prompts till the input is Valid.

the function get_word takes the level returned by get_level as input and returns the random word that will be guessed later and a number of tries. the word length and number of tries depends on the Level, one: 4 to 5 letters; 10 tries, two: 6 to 8 letters; 12 tries and three: 9 to 12 letters; 15 tries. to get the random word the wonderwords Library is used which should contain all English words. I considered using an API to a dictionary site but there were no completely free options. I also considered a txt file with all the possible words but that seemed extensive and doesn’t really allow for new words to be added over time.

the function guessing takes the random word, the level and the number of tries as input and exits if the win or lose conditions are met. first variables are initialized, "list_guesses" is for an overview of words or letters already guessed, "check" is also for overview it indicates the word length with a "_ " for each letter which will be replaced with correct letters later in the function, "count_guesses" is set to 0 and later increments for each guess. Then an Info is printed that all is set and the game begins. the rest of the function is inside a while loop so that several guesses can be made.
first "check" is printed using an empty string and .join() to concatenate the list into a string, followed by the information with the list_guesses and the remaining counts and the user is prompted for a guess. the guess is than checked, if it is already in list_guesses, so that guessing the same letter twice doesn’t cost a try. if the guess is not in list_guesses it will be appended to the list. If the guess is not a letter of the random word count_guesses is incremented. then the function graphics is called to print the corresponding graphics.
Next if the guess is a single Character and is a letter of the word, in a for loop going as long as the words length, each time the guess in the word, check is updated with the guess at the index equal to that in the word.
Then the win conditions are checked, if all letters of "check" form the right word or if the guess is the word the conditions are met the program exits with sys exit and the win message.
if the win conditions aren’t met the loosing conditions are checked, as soon as count_guesses is equal to tries the programs exits with the loosing message.
if neither condition is met the loop continues.
the function graphics takes count_guesses and level as input and returns a visualization. for count_guesses 1 to 9 are equal for all levels and builds piece by piece a Gallow. for count_guesses 10 and level 1 the hanged man is completed, for level 2 it's completed at count_guesses 12 and at 15 for level 3.
