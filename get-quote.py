import random
def main():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  quote = random.choice(quotes)

  print(quote)

if __name__== "__main__":
  main()
