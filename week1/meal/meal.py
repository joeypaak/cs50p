def main():
    time_input = input("What time is it? ")
    time = convert(time_input)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        return None


def convert(time):
    hours, minutes = map(int, time.split(":"))
    minutes = minutes / 60
    return hours + minutes


if __name__ == "__main__":
    main()
