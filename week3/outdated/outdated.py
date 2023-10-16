months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    month, day, year = get_date("Date: ")
    print(f"{year}-{month:02}-{day:02}")


def get_date(prompt):
    while True:
        date = input(prompt)
        # first case
        if len(date.split("/")) == 3:
            try:
                month, day, year = map(int, date.split("/"))
            except ValueError:
                pass
            else:
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return month, day, year
        # second case
        elif len(date.split()) == 3:
            month, day, year = date.split()
            if (
                day[len(day) - 1] == ","
                and month.title() in months
                and day.replace(",", "").isdecimal()
                and 1 <= int(day.replace(",", "")) <= 31
            ):
                month = months.index(month.title()) + 1
                try:
                    return month, int(day.replace(",", "")), int(year)
                except ValueError:
                    pass


main()
