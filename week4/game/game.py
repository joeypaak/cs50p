import random
import sys


def main():
    game(getLevel("Level: "))


def getLevel(prompt):
    while True:
        try:
            level = int(input(prompt))
        except ValueError:
            pass
        else:
            if level > 0:
                return level
            pass


def game(level):
    answer = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            else:
                sys.exit("Just right!")


if __name__ == "__main__":
    main()
