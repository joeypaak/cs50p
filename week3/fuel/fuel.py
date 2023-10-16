def main():
  percentage = get_fraction()
  print(percentage)

def get_fraction():
  while True:
    try:
      numerator, denominator = map(int, input("Fraction: ").split("/"))
      decimal = numerator / denominator
    except (ValueError, ZeroDivisionError):
      pass
    else:
      if 0 <= decimal <= 1:
        break

  percentage = int(round(decimal, 2) * 100)
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"


main()