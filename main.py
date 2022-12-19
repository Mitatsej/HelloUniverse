'''name = "Mitat"
last_name = "Sejdiu"
Full_name = name +" " + last_name
print("Emri im i plot eshte " + Full_name)'''
import time

'''height = 230.5
print("My height is " + str(height))#nese numri eshte flot ose int gjithe duhet me e kthy ne string per me u shfaq si ne kete shembull
'''

#Pranimi i inputav nga useri
'''name = input("What is your name: ")
age = int(input("How old are you: "))
height = float(input("How tall are you: "))

print("hello " + name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+" tall bisho")
'''
#kushtet
'''
age = int(input("How old are you: "))

if age == 100:
    print("You are an adult nowwwww!!!")
elif age < 0:
    print("You haven't born yet")
elif age >= 18:
    print("You are old mann don't givee uppp")
else:
    print("You are a child")'''

#Logical operator

'''temp = int(input("what a temp is outside: "))

if temp >= 0 and temp <= 30:
    print("The temp is good today")
    print("goooooo outside")
elif temp < 0 or temp > 30:
    print("The temp is bad today")
    print("Stay insideee man")
#not vendoset mas if edhe nese eshte mir ekthen keq nese osht keq e kthen mire dmth kontra
'''
#while loop dhe for looooooooooooooop
#while loop nuk osht e limitume kurse for loop eshte e limitume
'''while 1==1:
    print("helppppppp!!!!!!")
'''
'''
for seconds in range(10,0,-1):# caktohet sa numra me u shfaq     
    print(seconds)
    time.sleep(2)# sa sekonda me prit per mu shfaq numri tjetter
print("Urimee ditlindjaa")
'''
#nested loops
'''
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print() '''

#lists
'''food = ["hamburger","tatli" , "pudding" , "Spagetti"]

food.append("hotdog") # eshton
food.extend("hello") # eeemetodaaa tjera njejt
for x in food:
    print(x)
'''

#str.format() method
#{} kllapat perdoren si placeholder me shti ate fjal psh mrena fjalise.
#print("the {animal} run out to the {item}".format(animal="cow",item="moon"))


# me zgjedh vet kompjuteri diqka te rendomt psh
'''
import random
myList = ["rock","paper","scissors"] # e zgjedh here njeren her njeren
y = random.choice(myList)
print(y) '''

#exception handling/trajtimi i perjashtimeve
'''
try:
    numerator = int(input("Enter a numer to divide: "))
    denominator = int(input("Enter a numer divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("Nuk munesh me pjesto me zerro ! oshoq ka je nis!")
except ValueError as e:
    print(e)
    print("Ka je nisssss!!!!")
except Exception as e:
    print(e)
    print("Diqka ke shkru gabimm!!!")
else:
    print(result)
finally:
    print("Gjithemone ka me tu egzekutu")
'''

#Nese dojna me e kriju nje text ne projekt

'''
text = "hello bro \n This is some text\nSo ka je nisss!!!"
with open("test,txt" , "w") as file:
    file.write(text) #edhe u krijuuuuuuuu
'''
'''
# APP GAME  rock,papper scisors
import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices).lower()
    player = None

    while player not in choices:
        player = input("rock,paper or scissors?")

    if player ==computer :
        print("computer: ",computer)
        print("player: ",player)
        print("youu win shokiii")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("hupeee shokiii")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("fitovee shokiii")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("hupeee shokiii")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("fitovee shokiii")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("hupeee shokiii")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("fitovee shokiii")

    play_again = input("do you want to play again? : (yes/no)".lower())
    if play_again != "yes":
        break
print("byeeeee!!!!!") '''


#Quiiiiz  gameeee

'''
def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
      print("-------------------")
      print(key)
      for i in options[question_num-1]:
          print(i)
      guess = input("Enter (A,B,C or D): ")
      guess = guess.upper()
      guesses.append(guess)

      correct_guesses += check_answer(questions.get(key),guess)
      question_num += 1

      display_score(correct_guesses, guesses)

  #-----------------
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrongg!!!!")
        return 0
#-----------------
def display_score(correct_guesses , guesses):
    print("------------------")
    print("Results")
    print("------------------")

    print("Answers : ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses : ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " +str(score)+"%")

#-----------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
    #-----------------
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth  round?: ": "A"
}

options = [["A. Guido van Rossum","B. Elon Musk", "C. Bill Gates","D. Mark Zuckerburg"],
          ["A. 1989","B. 1991", "C. 2000","D. 2016"],
          ["A. Lonely Island","B. Smosh", "C. Monty Python","D. SNL"],
          ["A. True","B. False", "C. sometimes","D. What's Earth?"]]



new_game()

while play_again():
    new_game()

print("Byeeeeee!!!!")
'''