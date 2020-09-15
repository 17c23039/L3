from time import sleep
import random 
def calc () :
  number1 = float(input("Ima do some quick maths, gimme a number. "))
  sumtype = input("K, now give me an operator please. Like, add or smt. I can only rly do + - * and / bc im pretty simple. type help if ya need help. ")
  number2 = float(input("'kay, now gimme one more number "))
  if sumtype == "+" :
    print(float(number1 + number2))
  elif sumtype == "-" :
    print(float(number1 - number2))
  elif sumtype == "*" :
    print(float(number1 * number2))
  elif sumtype == "/" :
    print(float(number1 / number2))
  elif sumtype == "help" :
    print("Okay, so if you want me to add, then type + and then enter. Same with - for minus, * for multiply, and / for divide.")
    calc ()
  else :
    print("Error! You've entered something that we did not list. Please try again.")
  sleep(1)
  selection ()

def RPS () :
  rpsoutcome = random.randint(1, 3)
  if rpsoutcome == 1 :
    print("Rock!")
  elif rpsoutcome == 2 :
    print("Paper!")
  elif rpsoutcome == 3 :
    print("Scissors!")
  sleep(3)
  selection ()

def vs () :
  print("Okay, please standby while I scan your device for a virus. This should take no longer than  20 seconds.")
  vslength = random.randint(10, 120)
  sleep(vslength)
  print("We have found no viruses on your computer. Happy internet browsing!")
  sleep(1)
  selection ()
def trivia ():
  print("Hello! I am Trivia. I am going to quiz you on your general         knowledge! Please only use lowercase, as I am case sensitive. ")
  sleep(2)
  quest1 = input("What is the capital of Japan? ")
  if quest1 == "tokyo" :
    print("Correct!")
  elif quest1 == "Tokyo" :
    print("Correct, however remember. All lowercase please. You won't be given the correct later on. Let's continue.")
  else :
    print("Incorrect. It was Tokyo. Let's continue.")
  quest2 = input("What is 13 squared? ")
  if quest2 == "169" :
    print("Correct!")
  else :
    print("Incorrect. It was 169. Let's continue.")
  quest3 = input("What is the function used in python to show text on the screen? ")
  if quest3 == "print     " :
    print("Correct. 1 more to go!")
  else :
    print("That's wrong. It was 'print'")
  quest4 = input("Final question. What is the name of the song with the most views on YouTube as of 2018? ")
  if quest4 == "gangnam style" :
    print("Mhm. Correct. If you got 4/4, you got 100%, 3/4, 75, 2/4 is 50 and so on.")
  else :
    print("That's incorrect. It was Gangnam Style. If you got 4/4, you got 100%, 3/4, 75, 2/4 is 50 and so on.")
  print("Thanks for playing.")
  sleep(1)
  selection ()

def timer () :
  timerlength = float(input("Enter how long you would like to have your timer for (in seconds.) "))
  print("Okay, your timer will begin in...")
  sleep(1)
  print("3")
  sleep(1)
  print("2")
  sleep(1)
  print("1")
  sleep(1)
  print("Started.")
  sleep(timerlength)
  print("Done!")
  sleep(1)
  selection ()

def coinflip () :
  gamblecoin = input("Please choose heads or tails and your bet amount. Please type it in the format H/T.Uppercase or lowercase. I will not record your bet amount, so please don't type it. Thanks. ")
  outcomecoin = random.randint(1, 2)
  if outcomecoin == 1 :
    print("Heads!")
    if gamblecoin == "H" :
      print("Correct! You've won this bet.")
    elif gamblecoin == "h" :
      print("Correct! You have won this bet.")
    elif gamblecoin == "T" :
      print("Incorrect. You have lost this bet. Now go pay up.")
    elif gamblecoin == "t" :
      print ("Incorrect. You have lost this bet. Now go pay up.")
    else :
      print("Invalid option.")
  elif outcomecoin == 2 :
    print("Tails!")
    if gamblecoin == "T" :
      print("Correct! You've won this bet!")
    elif gamblecoin == "t" :
      print("Correct! You have won this bet!")
    elif gamblecoin == "H" :
      print("Incorrect. You have lost this bet. Now go pay up.")
    elif gamblecoin == "h" :
      print("Incorrect. You have lost this bet. Now go pay up.")
    else :
      print("Invalid option.")
  selection ()

def bingo () :
  print("The number is... (please note I cannot prevent numbers from repeating)")
  sleep (3)
  bingooutcome = random.randint(1, 30)
  print(bingooutcome)
  bingoanswer = input("Is the game over yet? Y/N ")
  if bingoanswer == "Y" :
    print("GG! Thanks for playing.")
    sleep (2)
    selection()
  elif bingoanswer == "N" :
    bingo ()


def lessonwork () :
  print("Nothing here so far!")
  selection ()
   
def selection () :
  print("Press 1 for Calculator.")
  print("Press 2 for Trivia.")
  print("Press 3 for Rock Paper Scissors.")
  print("Press 4 for Virus Scan.")
  print("Press 5 for Timer.")
  print("Press 6 for Lesson Work.")
  print("Press 7 for Coin Flip.")
  print("Press 8 for Bingo.")
  setting = input("Please select an option. ")
  if setting == "1" :
    calc ()
  elif setting == "2" :
    trivia ()
  elif setting == "3" :
    RPS ()
  elif setting == "4" :
    vs ()
  elif setting == "5" :
    timer ()
  elif setting == "6" :
    lessonwork ()
  elif setting == "7" :
    coinflip ()
  elif setting == "8" :
    bingo ()
  else :
    print("Error! Invalid option.")

selection ()