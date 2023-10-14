def main():
    camel_case = input("camelCase: ")
    snake_case = convert(camel_case)
    print(f"snake_case: {snake_case}")


def convert(string):
    new_string = []
    for char in string:
        if char.isupper():
            new_string.append(f"_{char.lower()}")
        else:
            new_string.append(char)
    return "".join(new_string)


main()
