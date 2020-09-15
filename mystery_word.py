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

# evil_mode = [
#     word.upper()
#     for word in text
# ]

def difficulty_mode():
    mode = input('Select mode (1 - Easy, 2 - Normal, 3 - Hard, 4 - Evil): ')
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
    

guessed_letters = []

def guessed_letters_list(guessed_letters):
    guess = input('Choose a letter')
    guessed_letters.apend(guess)
    return guessed_letters

def the_word(word, guessed_letters):
    return(letter if letter in guessed_letters else '__' for letter in word)

def try_again(word, guessed_letters):
    return sorted(set(
        letter
        for letter in guessed_letters
        if not letter in word
    ))

def play(word):
    guessed_letters = []
    while True:
        guesses_left = 8 - len(try_again(word, guessed_letters))
        print(f'Word: {" ".join(the_word(word, guessed_letters))}')
        print(f'Incorrectly guessed letters: {" ".join(try_again(word, guessed_letters))}')
        print(f'You have {guesses_left} guesses left')
        
        if '_' not in the_word(word, guessed_letters):
            print(f'Congrats! You guessed the right word')
            play_again()
            return
        guessed_letters = guessed_letters_list(guessed_letters)
        
        if guesses_left == 0:
            print(f"Oops you lose, the word was {word}")
            play_again()
            return
        guessed_letters = guessed_letters_list(guessed_letters)


def play_again():
    if input('Do you want to play again? (yes/no): ') == 'yes':
        new_game = difficulty_mode()
        play(new_game)
        return

if __name__ == "__main__":
    word = (difficulty_mode())
    play(word)