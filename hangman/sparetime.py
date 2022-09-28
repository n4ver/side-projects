import random


class Hangman:
    def __init__(self, path):
        self.words = self.wordlist(path)
        self.wrong_guesses = 5

        
    def screen(self, placeholder, guesses):
        print(placeholder)
        print()
        print("Wrong Guesses: ", end='') # Clean up
        print(*guesses, sep=", ")


    def wordlist(self, path):
        with open(path) as f:
            lst = [i.strip("\n") for i in f.readlines()]
            f.close()
        return lst


    def start(self):
        word = random.choice(self.words).lower()
        placeholder = self.create_placeholder(word)
        guesses = []
        self.gameloop(word, placeholder, guesses)


    def create_placeholder(self, word):
        length = len(word)
        placeholder = "_ " * length
        return placeholder.strip(" ")


    def update_placeholder(self, word, placeholder, guess):
        new_holder = ""
        placeholder = placeholder.replace(" ", "")
        for i in range(len(placeholder)):
            if placeholder[i] == " ": continue
            if placeholder[i] == "_":
                if word[i] == guess:
                    new_holder += guess + " "
                else:
                    new_holder += "_ "
            else:
                new_holder += placeholder[i] + " "
        return new_holder.strip(" ")


    def round(self, word, placeholder, guesses):
        self.screen(placeholder, guesses)
        guess = input("Give a guess: ")
        while not guess.isalpha() or len(guess) != 1 or guess in guesses:
            guess = input("Give a proper guess: ")
        if guess in word:
            placeholder = self.update_placeholder(word, placeholder, guess)
        else:
            guesses += [guess]
        return [placeholder, guesses]


    def gameloop(self, word, placeholder, guesses):
        while placeholder.replace(" ", "") != word:
            placeholder, guesses = self.round(word, placeholder, guesses)
            if len(guesses) > self.wrong_guesses:
                break
        if placeholder.replace(" ", "") == word:
            print("CONGRATULATIONS!!!")
        else:
            print("L")
        print(f"The word was: {word}")
        return


def main():
    game = Hangman(r"C:\Users\Nick\Desktop\wordlist.txt")
    game.start()

if __name__ == "__main__":
    main()
