import random
import string

class MultipleLettersError(Exception):
    pass
    
class NotLowercaseEnglishError(Exception):
    pass
    
class RepetitionError(Exception):
    pass

print("H A N G M A N")
print()
words = ('python', 'java', 'swift', 'javascript')
wins = 0
losses = 0
def play():
    global wins
    global losses
    attempts = 8
    guesses = set()
    while attempts > 0:
        print("".join(display))
        try:
            guess = input("Input a letter: ")
            if len(guess) != 1:
                raise MultipleLettersError

            elif guess not in string.ascii_lowercase:
                raise NotLowercaseEnglishError
        
            elif guess in guesses:
                raise RepetitionError
            else:
                letters = set(word)
                if guess not in letters:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                else:
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        if display[index] == "-":
                            display[index] = guess
                        else:
                            print("No improvements.")
                            attempts -= 1
                            break
        
            guesses.add(guess)
            
        except MultipleLettersError:
            print("Please, input a single letter.")
        except NotLowercaseEnglishError:
            print("Please, enter a lowercase letter from the English alphabet.")
        except RepetitionError:
            print("You've already guessed this letter.")  
        
    
        if "".join(display) == word:
            print(f"You guessed the word {word}!\nYou survived!")
            wins += 1
            break
        if attempts == 0:
            print("You lost!")
            losses += 1
            break
        print()
        
while True:
    user = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if user == "play":
        word = random.choice(words)
        display = list("-"*len(word))
        play()
    elif user == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
    else:
        break
