def main():
    x, y, z = input("Expression: ").split()
    x, z = int(x), int(z)
    output = float(calculate(x, y, z))
    print(output)


def calculate(x, y, z):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z


main()
