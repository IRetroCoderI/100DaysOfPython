# day 7 project - hangman
from words import words
import random
import hangman_art as hangman_art


# choose a random word

answer = random.choice(words)
tries = 7
hidden_word = '_'*len(answer)

#print("answer: " + answer)


def reveal_letter(hidden_word, letter_guess, answer):
    hidden_word = list(hidden_word)
    answer = list(answer)
    for i in range(0, len(hidden_word)):
        if answer[i] == letter_guess:
            hidden_word[i] = letter_guess
    hidden_word = "".join(hidden_word)
    answer = "".join(answer)
    return hidden_word

game_status = False #false for losing, true for winning

while tries-1 > 0:
    print(f'Word to guess: {hidden_word}')
    letter_guess = input("Guess a letter: ")
    if letter_guess in hidden_word:
        print(f'You\'ve already guessed {letter_guess}')
    elif letter_guess in answer:
        hidden_word = reveal_letter(hidden_word, letter_guess, answer)
        print(hidden_word)
        print(hangman_art.art[len(hangman_art.art) - tries])
        print(f"*******************************************{tries-1}/6 LIVES LEFT*******************************************")
        if hidden_word == answer:
            game_status = True
            break
    else:
        print(f'You guessed {letter_guess}, that\'s not in the word. You lose a life.')
        tries -= 1
        print(hangman_art.art[len(hangman_art.art) - tries])
        print(f"*******************************************{tries-1}/6 LIVES LEFT*******************************************")


if not game_status:
    print(hangman_art.game_over_art)
else:
    print(hangman_art.winning_art)


print("The answer was: " + answer +"!")

