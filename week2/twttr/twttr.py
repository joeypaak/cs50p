def main():
    string = input("Input: ")
    output = twttr(string)
    print(f"Output: {output}")


def twttr(string):
    new_string = []
    for char in string:
        if vowel(char.lower()):
            new_string.append("")
        else:
            new_string.append(char)
    return "".join(new_string)


def vowel(char_lowered):
    if (
        char_lowered == "a"
        or char_lowered == "e"
        or char_lowered == "i"
        or char_lowered == "o"
        or char_lowered == "u"
    ):
        return True
    else:
        return False


main()
