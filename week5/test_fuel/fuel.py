def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    # turn X, Y into integers
    try:
        x, y = map(int, fraction.split("/"))
    except ValueError:
        raise ValueError

    # divide and get the decimal
    try:
        z = x / y
    except ZeroDivisionError:
        raise ZeroDivisionError

    # when X is greater than Y
    if x > y:
        raise ValueError
    
    return int(round(z * 100, 0))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
