import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # TODO: “No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c in string.punctuation:
            return False

    s_length = len(s)
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    # TODO: "not 2 <= s_length <= 6"
    if not 2 <= s_length <= 6:
        return False
    # all vanity plates must start with at least two letters
    # TODO: "s_length == 2"
    elif not s[:2].isalpha():
        return False
    # The first number used cannot be a ‘0’
    # TODO: "s_length == 3"
    elif s_length >= 3:
        if s[2] == "0":
            return False

    # TODO: "s_length == 4"
    if s_length == 4:
        # whether if last char is not a digit but the string contains a number
        if contains_numbers(s) and not s[3].isdigit():
            return False
    elif s_length == 5:
        if contains_numbers(s):
            # if the last char is not a digit, return False
            if not s[4].isdigit():
                return False
            # else if the 3rd char is a digit and 4th is not a digit, return False
            elif s[2].isdigit() and not s[3].isdigit():
                return False
    elif s_length == 6:
        if contains_numbers(s):
            if s[5].isdigit():
                # from six combinations, only two is valid
                if ((not s[2].isdigit()) and (not s[3].isdigit()) and s[4].isdigit()) or (
                    (not s[2].isdigit()) and (s[3].isdigit()) and s[4].isdigit()
                ):
                    pass
                else:
                    return False
            else:
                return False

    # If there's no problem, return True
    return True


def contains_numbers(s):
    for char in s:
        if char.isdigit():
            return True


if __name__ == "__main__":
    main()
