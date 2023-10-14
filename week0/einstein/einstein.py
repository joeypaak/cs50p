def main():
    energy = calE()
    print(f"E: {energy}")


def calE():
    mass = int(input("m: "))
    return mass * 300000000**2


main()
