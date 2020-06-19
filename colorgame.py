#import modules
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Colour Game")
root.geometry("375x200")
root.configure(background="SpringGreen2")

colours = ['RED', 'PURPLE', 'WHITE', 'ORANGE', 'PINK', 'BROWN', 'GREEN', 'YELLOW', 'BLUE']
score = 0
timeleft = 30               #Time limit of 30 seconds

#Fnction to start Game
def startGame(event):
    if timeleft == 30:
        countdown()         #start timer
    nextColour()            #choose next colour

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        #if colours are equal: increment score
        if e.get().lower() == colours[1].lower():
            score += 1
        #clear entry box
        e.delete(0, END)
        random.shuffle(colours)
        label.config(bg='SpringGreen2', fg=str(colours[1]), text = str(colours[0]))
        scoreLabel.configure(text="Score: "+str(score))

    if timeleft == 0:
        messagebox.showinfo("Time is Up!!", "Score: "+str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1           #Reduce by 1
        #Display Updated time left
        timeLabel.configure(text = "Time Left: " + str(timeleft) + " seconds")
        #Run function after 1000 seconds
        timeLabel.after(1000,countdown)

#Instruction Label
instruction = Label(root, bg='SpringGreen2', fg='black', text = "Type the colour of the words and not the word!", font = ("Helvetica", 12, 'bold'))
instruction.pack()

#Add Score Label
scoreLabel = Label(root, bg='SpringGreen2', fg='black', text = "Press Enter to start", font = ("Helvetica", 12, 'bold'))
scoreLabel.pack()

#Add Time Left Label
timeLabel = Label(root, bg='SpringGreen2', fg='black', text = "Time Left: " + str(timeleft), font = ("Helvetica", 12, 'bold'))
timeLabel.pack()

#label for displaying colours
label = Label(root, bg='SpringGreen2', font = ("Helvetica", 30, 'bold'))
label.pack()

#Entry box for user to type colour
e=Entry(root)

#Start Game on Press of Enter Key
root.bind('<Return>', startGame)
e.pack()

#set focus on entry box
e.focus_set()

root.mainloop()
