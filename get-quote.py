import random

def primary():
  #print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for quote in quotes:
    print(quotes[random.randint(0, len(quotes) - 1)].strip())
    f = open("results.txt")
    f.write("quote")
    f.close()



if __name__== "__main__":
  primary()
