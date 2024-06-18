from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    number = random.randint(1,3)
    # 2. Print your variable to the console
    print(str(number))
    # 3. Get the user to enter something that they think is awesome
    word = input("Enter something you think is awesome!")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!

    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if number == 1:
        print(str(word) + " is/are ok")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if number  == 2:
        print(str(word) + " is/are boring")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if number == 3:
        print(str(word) + " is/are AWESOME")

    # Run the window's .mainloop() method
    window.mainloop()