def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    print(d[1:])
    return float(d[1:])


def percent_to_float(p):
    # TODO
    print(p[:2])
    return 0.01 * int(p[:2])


main()