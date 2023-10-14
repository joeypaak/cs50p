import sys
import requests


def main():
    # Check if the CLA is valid
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif not isFloat(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    elif float(sys.argv[1]) < 0:
        sys.exit("Command-line argument is not a positive number")

    # Send request
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit(
            "There was an ambiguous exception that occurred while handling your request"
        )
    else:
        price = r["bpi"]["USD"]["rate_float"]

    # Print out
    print(f"${price * float(sys.argv[1]):,.4f}")


def isFloat(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True


main()
