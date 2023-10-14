def main():
    amount_due = 50
    while True:
        amount_due -= insert_coin(amount_due)
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {-amount_due}")
            break


def insert_coin(x):
    while True:
        coin = int(input("Insert Coin: "))
        if coin != 5 and coin != 10 and coin != 25:
            print(f"Amount Due: {x}")
        else:
            return coin


main()
