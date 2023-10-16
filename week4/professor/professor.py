import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        if round(level):
            score += 1
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            level = int(level)
            return level


def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    elif level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10**level - 1)


def round(level):
    wrong = 0
    x, y = generate_integer(level), generate_integer(level)
    answer = x + y
    while True:
        try:
            guess = int(input(f"{x} + {y} = "))
        except ValueError:
            pass
        else:
            if guess == answer:
                return True
            elif wrong != 2:
                print("EEE")
                wrong += 1
            else:  # if wrong == 2
                print("EEE")
                print(f"{x} + {y} = {answer}")
                return False


if __name__ == "__main__":
    main()
