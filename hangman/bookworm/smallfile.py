#import cProfile
import os

weightTiles = {"a":1,
               "d":1,
               "e":1,
               "g":1,
               "i":1,
               "l":1,
               "n":1,
               "o":1,
               "r":1,
               "s":1,
               "t":1,
               "u":1,
               "b":1.25,
               "c":1.25,
               "f":1.25,
               "h":1.25,
               "m":1.25,
               "p":1.25,
               "v":1.5,
               "w":1.5,
               "y":1.5,
               "j":1.75,
               "k":1.75,
               "q":1.75,
               "x":2,
               "z":2,
               }


def spellable(word, tiles):
    word_count = count_letters(word)
    tile_count  = count_letters(tiles)
    try:
        return all( [word_count[letter] <= tile_count[letter] for letter in word] )
    except KeyError:
        return False


def convertTuple(tup):
    string = ''.join(tup)
    return string


def scoreTile(word):
    return sum([weightTiles[letter] for letter in word])


def count_letters(word):
    # super unoptimised
    count = {} 
    for letter in word:
        if letter not in count: count[letter] = 0
        count[letter] += 1 
    return count


# input format: letters without spacing, Q stands for Qu
# eg. abcdefghijklmnop


def main():
    pagelimit = 20
    with open('words1.txt','r') as fp:
        words = fp.read().splitlines()
    temp = True
    sortstyle = input("Input sort style (score/length): ")
    while sortstyle not in ("score", "length"):
        sortstyle = input("Input sort style (score/length): ")
    while temp:
        num = 0
        currentTiles = input("Enter tiles: ")
        while not currentTiles.isalpha() or len(currentTiles) > 16:
            currentTiles = input("Enter valid tiles: ")
        currentTiles = currentTiles.lower()
        
        available = []
        results = set()
        for k in currentTiles:
            if k != "q":
                available += [k]
            else:
                available += [k + "u"]
                
        for word in words:
            if spellable(word, available):
                results.add(word)

        resultlist = list(results)
        if sortstyle == "length":
            resultlist.sort(key=len,reverse=True)
        else:
            resultlist.sort(key=scoreTile,reverse=True)
        if len(results) == 0:
            print("No words available")
        else:
            print("Search found {} words.".format(len(results)))
            print("Showing first {} words.".format(pagelimit))
            print("{:<18}{:<8}{:<7}".format("word", "length", "score"))
        for i in resultlist:
            if num > pagelimit:
                break
            else:
                print("{:<18}{:<8}{:<7}".format(i, len(i), scoreTile(i)))
            num += 1
        x = input("Continue? (y/n): ")
        x = x.lower()
        if x not in ("y", "n"):
            x = input("Continue? (y/n): ")
        if x == "y":
            os.system('cls')
        else:
            temp = False
            os.system("pause")


if __name__ == "__main__":
    main()
    # cProfile.run('main()')
