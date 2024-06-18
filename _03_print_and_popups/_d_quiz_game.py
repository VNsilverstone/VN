from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window =Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
Question1 = input("True or False, does 1+1=2")
    #      // 3.  Use an if statement to check if their answer is correct
if Question1 == ("true") or Question1 == ("True"):
    print("Good Job, Your Correct")
    score = score + 1
    print("Your Score = " + str(int(score)))
else:
    if Question1 == ("false") or Question1 == ("False"):
        print("Wrong")
    score  = score - 1
    print("Your Score = " + str(int(score)))

    #      // 4.  if the user's answer was correct, add one to their score 

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer#
Question2 = input("True or False. Lions are weak compared to humans")
if Question2 == ("True") or Question2 == ("true"):
    print("Wrong.")
    score = score - 1
    print("Your Score = " + str(int(score)))
else:
    if Question2 == ("False") or Question2 == ("false"):
        print("Correct")
    score = score + 1
    print("Your score = " + str(int(score)))
Question3 = input("True or False, 3497547574374543745484554x455454345434543 is 1.5929732e+39")
if Question3 == ("True") or Question3 == ("true"):
    print("Correct")
    score = score + 1
    print("Your Final Score = " + str(int(score)))
else:
    if Question3 == ("False") or Question3 == ("false"):
        print("Wrong")
        score = score - 1
    print("Your Final Score = " + str(int(score)))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 

    # Run the window's .mainloop() method
    window.mainloop()