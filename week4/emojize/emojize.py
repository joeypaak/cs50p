from emoji import emojize


def main():
    s = input("Input: ")
    print(f"Output: {emojize(s, language='alias')}")


if __name__ == "__main__":
    main()
