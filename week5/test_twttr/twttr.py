replacements = [
    ("a", ""),
    ("e", ""),
    ("i", ""),
    ("o", ""),
    ("u", ""),
    ("A", ""),
    ("E", ""),
    ("I", ""),
    ("O", ""),
    ("U", ""),
]


def main():
    userInput = input("Input: ")
    output = shorten(userInput)
    print(f"Output: {output}")


def shorten(string):
    for old, new in replacements:
        string = string.replace(old, new)
    return string


if __name__ == "__main__":
    main()
