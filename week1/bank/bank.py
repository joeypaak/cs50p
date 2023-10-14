def main():
    greeting = input("Greeting: ").lower()
    print(money(greeting))

def money(g):
    if "hello" in g:
        return "$0"
    elif g[0] == "h":
        return "$20"
    else:
        return "$100"

main()
