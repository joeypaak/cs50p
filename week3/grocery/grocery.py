grocery = {}

def main():
  while True:
    try:
      single_item = input()
    except EOFError:
      print("")
      for item in sorted(grocery.keys()):
        print(f"{grocery[item]} {item.upper()}")
      break
    else:
      try:
        grocery[single_item] += 1
      except KeyError:
        grocery[single_item] = 1


main()