# NAME OF AUTHOR: Carter King (CK-OCSB)
# NAME OF THE PROGRAM: Math Practice  
# DATE OF CREATION: 2022-01-28 ,  
# PURPOSE OF PROGRAM: To provide a series of math problems to the user. The user will chose the type of questions as well as the difficulty.  

# INPUT
print("Welcome to Math Practice! \nIn this program your math skills will be tested! \nYou will chose the category of your questions as well as the difficulty of your choosing.")
MathChoise = str(input('What kind of math would you like to practice? \nIf you would like to choose addition type "Add" \nIf you would like to chose subtraction type "Sub" \nIf you would like to choose Multiplication type "Multi" \nIf you would like to chose Division type "Div" \nWhat would you like to choose:'))
if MathChoise:
    DiffSet = int(input('The difficulty of for this practice ranges from 1 to 5, \n1 is the the easiest and 5 being the hardest, the harder the difficulty, the more amount of questions you will have to answer even harder questions!  \nPlease select a difficulty by typing a number:'))


# VARIABLE DEFINITION
import random

####### Settings for the difficulty#########
if DiffSet == 1:
    QuestionAmmount = 10
if DiffSet == 2:
    QuestionAmmount = 20
if DiffSet == 3:
    QuestionAmmount = 35
if DiffSet == 4:
    QuestionAmmount = 50
if DiffSet == 5:
    QuestionAmmount = 75
###################
if DiffSet == 1:
    SubRange1 = random.randint(1,20)
    SubRange2 = random.randint(1,25)
    SubTotal = SubRange1 + SubRange2
if DiffSet == 2:
    SubRange1 = random.randint(1,30)
    SubRange2 = random.randint(1,45)
    SubTotal = SubRange1 + SubRange2
if DiffSet == 3:
    SubRange1 = random.randint(1,50)
    SubRange2 = random.randint(1,50)
    SubTotal = SubRange1 + SubRange2
if DiffSet == 4:
    SubRange1 = random.randint(1,60)
    SubRange2 = random.randint(1,75)
    SubTotal = SubRange1 + SubRange2
if DiffSet == 5:
    SubRange1 = random.randint(1,100)
    SubRange2 = random.randint(1,85)
    SubTotal = SubRange1 + SubRange2
    #################
if DiffSet == 1:
    MultiRange1 = random.randint(1,5)
    MultiRange2 = random.randint(1,10)
    MultiTotal = MultiRange1 + MultiRange2
if DiffSet == 2:
    MultiRange1 = random.randint(1,10)
    MultiRange2 = random.randint(1,10)
    MultiTotal = MultiRange1 + MultiRange2
if DiffSet == 3:
    MultiRange1 = random.randint(1,12)
    MultiRange2 = random.randint(1,12)
    MultiTotal = MultiRange1 + MultiRange2
if DiffSet == 4:
    MultiRange1 = random.randint(5,12)
    MultiRange2 = random.randint(5,14)
    MultiTotal = MultiRange1 + MultiRange2
if DiffSet == 5:
    MultiRange1 = random.randint(1,15)
    MultiRange2 = random.randint(5,20)
    MultiTotal = MultiRange1 + MultiRange2
    ####################
if DiffSet == 1:
    DivRange1 = random.randint(1,3)
    DivRange2 = random.randint(1,30)
    DivTotal = DivRange1 + DivRange2
if DiffSet == 2:
    DivRange1 = random.randint(1,5)
    DivRange2 = random.randint(1,60)
    DivTotal = DivRange1 + DivRange2
if DiffSet == 3:
    DivRange1 = random.randint(1,7)
    DivRange2 = random.randint(1,80)
    DivTotal = DivRange1 + DivRange2
if DiffSet == 4:
    DivRange1 = random.randint(1,10)
    DivRange2 = random.randint(1,100)
    DivTotal = DivRange1 + DivRange2
if DiffSet == 5:
    DivRange1 = random.randint(1,10)
    DivRange2 = random.randint(1,150)
    DivTotal = DivRange1 + DivRange2
#########################
CorrectAnswers = 0
IncorrectAnswers = 0 
# PROCESSING

###################

if MathChoise == ("Add"):
 print("You have chosen addition your questions begin NOW!")

while MathChoise == ("Add") and DiffSet == 1 and QuestionAmmount > 0:
  AddRange1 = random.randint(1,40)
  AddRange2 = random.randint(1,40)
  print("Your questions is",AddRange1,"+",AddRange2)
  UserAnswer = int(input("Your answer is : "))
  AddTotal = AddRange1 + AddRange2
  if UserAnswer == AddTotal :
    CorrectAnswers = CorrectAnswers + 1 
  if UserAnswer != AddTotal:
    IncorrectAnswers = IncorrectAnswers + 1
  if UserAnswer:
    QuestionAmmount = QuestionAmmount - 1

while MathChoise == ("Add") and DiffSet == 2:
    AddRange1 = random.randint(1,75)
    AddRange2 = random.randint(1,75)
    print("Your questions is",AddRange1,"+",AddRange2)
    UserAnswer = int(input("Your answer is : "))
    AddTotal = AddRange1 + AddRange2
    if UserAnswer == AddTotal :
      CorrectAnswers = CorrectAnswers + 1 
    if UserAnswer != AddTotal:
      IncorrectAnswers = IncorrectAnswers + 1
while MathChoise == ("Add") and DiffSet == 3:
    AddRange1 = random.randint(1,100)
    AddRange2 = random.randint(1,100)
    print("Your questions is",AddRange1,"+",AddRange2)
    UserAnswer = int(input("Your answer is : "))
    AddTotal = AddRange1 + AddRange2
    if UserAnswer == AddTotal :
      CorrectAnswers = CorrectAnswers + 1 
    if UserAnswer != AddTotal:
      IncorrectAnswers = IncorrectAnswers + 1
while MathChoise == ("Add") and DiffSet == 4:
    AddRange1 = random.randint(1,150)
    AddRange2 = random.randint(1,150)
    print("Your questions is",AddRange1,"+",AddRange2)
    UserAnswer = int(input("Your answer is : "))
    AddTotal = AddRange1 + AddRange2
    if UserAnswer == AddTotal :
      CorrectAnswers = CorrectAnswers + 1 
    if UserAnswer != AddTotal:
     IncorrectAnswers = IncorrectAnswers + 1
while MathChoise == ("Add") and DiffSet == 5:
    print("Your questions is",random.randint(1,200),"+",random.randint(1,200))
    UserAnswer = int(input("Your answer is : "))
    AddTotal = AddRange1 + AddRange2
    if UserAnswer == AddTotal :
      CorrectAnswers = CorrectAnswers + 1 
    if UserAnswer != AddTotal:
      IncorrectAnswers = IncorrectAnswers + 1



if QuestionAmmount == 0:
    print("You answered",CorrectAnswers,"questions correctly.\nYou answered",IncorrectAnswers,"incorrectly. \nYou did this on difficulty",DiffSet)
    print("Practice some more! Maybe try a harder difficulty")




