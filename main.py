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
  rpsinput = input("Enter your selection. Don't worry, I do not cheat. R/P/S. Use uppercase please. ")
  rpsoutcome = random.randint(1, 3)
  print("Rock...")
  sleep(1)
  print("Paper...")
  sleep (1)
  print("Scissors...")
  sleep(1)
  if rpsoutcome == 1 :
    print("Rock!")
    sleep (1)
    if rpsinput == "R" :
      print("It's a tie!")
    elif rpsinput == "P" :
      print("Wow, you win :D")
    elif rpsinput == "S" :
      print("Ha! I win!")
    else :
      print("Invalid option!")
      sleep(1)
      RPS ()
  elif rpsoutcome == 2 :
    print("Paper!")
    sleep(1)
    if rpsinput == "R" :
      print("Ha! I win!")
    elif rpsinput == "P" :
      print("It's a tie!")
    elif rpsinput == "S" :
      print("Wow, you win :D")
    else :
      print("Invalid option.")
      sleep(1)
      RPS ()
  elif rpsoutcome == 3 :
    print("Scissors!")
    if rpsinput == "R" :    
      print("Wow, you beat me :D")
    elif rpsinput == "P" :
      print("Ha! I win!")
    elif rpsinput == "S" :    
      print("It's a tie!")
    else :
      print("Invalid option!")
      sleep(1)
      RPS ()
  sleep(3)
  playagain = input("Play again? Y/N ")
  if playagain == "Y" :
    RPS()
  elif playagain == "N" :
    selection ()

def vs () :
  print("Okay, please standby while I scan your device for a virus. This should take no longer than 2 minutes.")
  vslength = random.randint(10, 120)
  sleep(vslength)
  print("We have found no viruses on your computer. Happy internet browsing!")
  sleep(1)
  selection ()

def trivia ():
  print("Hello! I am Trivia. I am going to quiz you on your general knowledge! Please only use lowercase, as I am case sensitive. ")
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
  if quest3 == "print" :
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
  gamblecoin = input("Please choose heads or tails. Please type it in the format H/T.Uppercase or lowercase. ")
  outcomecoin = random.randint(1, 2)
  if outcomecoin == 1 :
    print("Heads!")
    if gamblecoin == "H" :
      print("Correct! You've won.")
    elif gamblecoin == "h" :
      print("Correct! You have won.")
    elif gamblecoin == "T" :
      print("Incorrect. You have lost.")
    elif gamblecoin == "t" :
      print ("Incorrect. You have lost.")
    else :
      print("Invalid option.")
  elif outcomecoin == 2 :
    print("Tails!")
    if gamblecoin == "T" :
      print("Correct! You've won!")
    elif gamblecoin == "t" :
      print("Correct! You have won!")
    elif gamblecoin == "H" :
      print("Incorrect. You have lost.")
    elif gamblecoin == "h" :
      print("Incorrect. You have lost.")
    else :
      print("Invalid option.")
  sleep(1)
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

def rng () :
  print("Please choose the highest and lowest values you'd like.")
  lowestvalue = float(input("Lowest number: "))
  sleep (0.5)
  highestvalue = float(input("Highest number: "))
  print()
  print("Thanks, printing your numbers...")
  sleep (2)
  rngoutput = random.randint(lowestvalue, highestvalue)
  print(rngoutput)
  sleep(2)
  selection ()

def madlibs () :

  madlibsstory = float(input("What story would you like? 1/2. "))
  if madlibsstory == 1 :
    print("Okay, generating story...")
    sleep(3)
    noun1 = input("Give me a noun. ")
    place1 = input("Give me a place. ")
    emotion1 = input("Give me an emotion. ")
    verb1 = input("Give me a verb. ")
    noun2 = input("Give me another noun. ")
    adjective1 = input("Give me an adjective. ")
    noun3 = input("Give me a third noun. ")
    noun4 = input("Give me a fourth noun. ")
    noun5 = input("Give me a final noun. ")
    verb2 = input("Give me a verb. ")
    name1 = input("Give me a name. ")
    print("Thanks. Generating your story...")
    sleep (5)
    print()
    print(f"One day there was a {noun1} who lived in {place1}. This {noun1} was very {emotion1} and he was so {emotion1} he decided to {verb1} in a {noun2}. What a {adjective1} thing to do! Later that day, he died due to a {noun3}, {noun4} and a {noun5} which all {verb2}ed him.")
    print(f"-{name1}")
    madlibsrestart = input("Go again? Y/N")
    if madlibsrestart == "Y" :
      madlibs() 
    elif madlibsrestart == "N" :
      selection() 
    else :
      print("Invalid option! Redirecting to selection...")
      selection() 

  elif madlibsstory == 2 :
    print("Okay, generating story...")
    sleep(3)
    adjective1 = input("Give me an adjective. ")
    noun1 = input("Give me a noun. ")
    adjective2 = input("Give me an adjective. ")
    noun2 = input("Give me a noun.")
    verb1 = input("Give me a verb. ")
    noun3 = input("Give me a noun. ")
    verb2 = input("Give me a verb. ")
    noun4 = input("Give me a noun. ")
    noun5 = input("Give me a noun. ")
    adjective3 = input*("Give me an adjective. ")
    verb3 = input("Give me a verb. ")
    noun6 = input("Finally, give me a noun.")
    print("Thanks, generating story...")
    sleep(5)
    print("Dear Diary,")
    print(f"Today was {adjective1}! This morning, I ate some {noun1} and it was {adjective2}. Then, I went to school in a {noun2}. At school, I {verb1}ed at the {noun3}, and then I {verb2}ed at the {noun4}. When I came home, my parents gave me a present! Inside was a {noun5} and it was so {adjective3}. Then, I {verb3}ed with James and then I went to sleep in my {noun6}.")
    if madlibsrestart == "Y" :
      madlibs() 
    elif madlibsrestart == "N" :
      selection() 
    else :
      print("Invalid option! Redirecting to selection...")
      selection() 

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
  print("Press 9 for Random Number Generator.")
  print("Press 10 for Mad Libs")
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
  elif setting == "9" :
    rng ()
  elif setting == "10" :
    madlibs ()
  else :
    print("Error! Invalid option.")

selection ()