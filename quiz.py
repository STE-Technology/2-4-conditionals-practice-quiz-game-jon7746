"""
File: quiz.py
Author: Jonathan Benvenuto
Date: 2007-03-05
Description: Quizing the genral public.
"""

print("|-------------------- Are you smarter than a 5th grader? --------------------|")

#Setting up the counter system
counter = 0

#Outputs the first question
print("Multiple-Choice Quiz Game\n")
print("1.What is the capital of France\n \
    (a) Paris\n \
    (b) London\n \
    (c) Rome\n")

#Asking user for the answer
answer = input("> ")

#Checks if the answer is right or wrong
if (answer == "A") or (answer == "a"):
   
   #Outputs if the answer is correct
    print("Correct!\n")

    #Adds one to the score if correct
    counter += 1

else:
    
    #Outputs if the answer is incorrect
    print("WOMP WOMP Incorrect!\n")
    
#Outputs the second question
print("2. Which planet is known as the Red Planet?\n \
    (a) Mars\n \
    (b) Venus\n \
    (c) Jupiter\n")

#Asking user for the answer
answer = input("> ")

#Checks if the answer is right or wrong
if (answer == "A") or (answer == "a"):
   
    #Outputs if the answer is correct
    print("Correct!\n")

    #Adds one to the score if correct
    counter += 1

else:
    
    #Outputs if the answer is incorrect
    print("WOMP WOMP Incorrect!\n")

#Outputs the third question
print("3. Who painted the Mona Lisa?\n \
    (a) Leonardo da Vinci\n \
    (b) Pablo Picasso\n \
    (c) Vincent van Gogh\n")

#Asking user for the answer
answer = input("> ")

#Checks if the answer is right or wrong
if (answer == "A") or (answer == "a"):
   
    #Outputs if the answer is correct
    print("Correct!\n")

    #Adds one to the score if correct
    counter += 1

else:
    
    #Outputs if the answer is incorrect
    print("WOMP WOMP Incorrect!\n")

#Computes final score
score = round((counter / 3) * 100, 1)

#Outputs ending message and final score
print("QUIZ COMPLETE!")
print("You answered " + str(counter) + " out of 3 questions correctly. Your score is " + str(score) + ("%"))