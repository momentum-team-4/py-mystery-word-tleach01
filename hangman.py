import random
import string

file = open("words.txt")
text = file.read().split()

easy_mode = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]
normal_mode = [
     word.upper()
    for word in text
    if 6 <= len(word) <= 8
]
hard_mode = [
     word.upper()
    for word in text
    if 8 <= len(word) 
]

def difficulty_mode():
    mode = input('Select mode (1 - Easy, 2 - Normal, 3 - Hard): ')
    if mode == '1':
        word = random.choice(easy_mode)
    elif mode == '2':
        word = random.choice(normal_mode)
    elif mode == '3':
        word = random.choice(normal_mode)
    else:
        return difficulty_mode
    print(f'The word has {len(word)} letters.')
    return word
    

def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print("Let's play!")
    print(display_hangman(tries))
    print(word_complete)
    while not guessed and tries > 0:
        guess = input("Guess your first letter!")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed that letter', guess)
            elif guess not in word:
                print (guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('That is in the word.')
                guessed_letters.append(guess)
                word_list = list(word_complete)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                 # enumerate "allows us to loop over something and have an automatic counter"
                for index in indexes:
                    word_complete = ''.join(word_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                    print('You already guessed the word')
            elif guess != word:
                    print(guess, 'is not the word')
                    tries -= 1
                    guessed_words.append(guess)
            else:
                    guessed = True
                    word_complete = word
        else:
            print('Not a valid guess')
        print(display_hangman(tries))
        print(word_complete)
        if guessed:
            print('Congrats! You got the word right!')
        else:
            print('Sorry, you lose. The word was' + word)


def display_hangman(tries):
    hangman = [
         """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return hangman[tries]

def main():
    if input('Play again? (Yes/No)').upper() == 'Y':
        word = difficulty_mode()
        play(word)
        return

if __name__ == "__main__":
    main()