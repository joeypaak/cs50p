def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Getting ready for checking
    # length of the string
    s_len = len(s)
    # if there are any digits within the string
    contains_numbers = False
    for i in range(s_len):
        if s[i].isdigit():
            contains_numbers = True
            break

    # check if the first two characters are letters
    if not s[:2].isalpha():
        return False
    # check if 2 <= length <= 6
    if not 2 <= s_len <= 6:
        return False
    # check if there are periods, spaces, or punctuation marks
    for char in s:
        if (char.isalpha() or char.isdigit()) == False:
            return False
    # check if first number is zero
    if contains_numbers:
        first_num = None
        first_num_location = None
        for i in range(s_len):
            if s[i].isdigit():
                first_num = int(s[i])
                first_num_location = i
                break
        if first_num == 0:
            return False
        # check if numbers are only at the end
        if not s[first_num_location:].isdigit():
            return False

    return True


main()
