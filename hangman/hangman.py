import cProfile
import time
from random import choice


def validate(correct_guesses, wrong_guesses, char):
    if len(char) != 1: return False
    if not char.isalpha(): return False
    if char in correct_guesses: return False
    if char in wrong_guesses: return False
    return True


def read_from_file():
    filename = "words.txt"
    f = open(filename, "r")
    words = [i.strip("\n").lower() for i in f.readlines()]
    return words


def print_word(lst):
    string = ''.join(lst)
    print(string)


def conv_set_to_str(the_set):
    # ['a', 'b', 'c']
    if len(the_set) == 0:
        return "None"
    lst = list(the_set)
    length = len(lst)
    string = ("{}, "*length).format(*lst).strip(", ")
    return string

def main():
    guesses_left = 10
    won = False
    wordlist = read_from_file()
    word = choice(wordlist)
    length = len(word)
    hang_list = ["_"]*length
    word_list = list(word)
    wrong_guesses = set()
    correct_guesses = set()
    while guesses_left != 0:
        if hang_list == list(word):
            print("You won!")
            break
        print("Length: {}\nGuesses Left: {}\nWrong Guesses: {}".format(length, guesses_left, conv_set_to_str(wrong_guesses)))
        print_word(hang_list)
        guess = input("Enter guess: ")
        while not validate(correct_guesses, wrong_guesses, guess):
            guess = input("Enter valid guess: ")
        guess = guess.lower()
        if guess not in word_list:
            wrong_guesses.add(guess)
            guesses_left -= 1
        else:
            correct_guesses.add(guess)
        while guess in word_list:
            temp = word_list.index(guess)
            word_list[temp] = "_"
            hang_list[temp] = guess
    else:
        print("You lost! The word was {}".format(word))
    return

if __name__ == "__main__":
    main()
