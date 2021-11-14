# Author: Johnsons Sangah
# Date created: 7 Oct 2021
# Date last changed: 18 Oct 2021

#  This program allows a user to calculate their own BMI user their own height and weight. It also allows a user to
# select from a list of names given to display their BMI and corresponding BMI Classification as per the ranges
# outlined by the Department of Health. This program was made for an Assignment whilst enrolled into Introduction to
# Information Technology at the University of Canberra.

#  Input: data entered by user, Output: none

from tkinter import *

window = Tk()
FONT = "Calibre 11"
BLANK_VALUE = ""
WELCOME = "Welcome to the BMI calculator! It's so good to see you interested in understanding more about your health."
BMI_COLOUR = "blue"

# An instance of the class TK is created and a title provided.
window.title("BMI Calculator")


# ***********************************************************************************************************************
# All my user-defined functions
def entryBMIClassifcation(calculated_bmi):
    if calculated_bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= calculated_bmi < 25:
        return 'Healthy Weight'
    elif 24.9 < calculated_bmi < 30:
        return 'Overweight but not obese'
    elif 29.9 < calculated_bmi < 35:
        return 'Obese class I'
    elif 34.9 < calculated_bmi < 40:
        return 'Obese class II'
    else:
        return 'Obese class III'


# BMI Calculation function for values entered to the entry widgets.

def entryBMICalculation(weight, height):
    bmi = round(weight / (height ** 2), 2)
    print(bmi)
    contOfBMI.set(bmi)
    contOfBMIClassification.set(entryBMIClassifcation(bmi))
    return bmi


def btnReset():
    entWeight.delete(0, END)
    entWeight.insert(0, 'in kg')
    entHeight.delete(0, END)
    entHeight.insert(0, 'in metres')
    contOfBMI.set("")
    contOfBMIClassification.set("")


# Separate user-defined functions to clear the contents in the height and weight Entry widgets. Having separate
# functions ensures that the contents are cleared for that box when the user clicks to enter a value.
def clearEntryWidgetHeight(event):
    entHeight.delete(0, END)


def clearEntryWidgetWeight(event):
    entWeight.delete(0, END)


def selectUser(event):
    item = lstNE.get(lstNE.curselection())
    key = item.lower()
    #     # Get the weight and height from the dictionary, and use it to calculate the BMI for the selected user.
    intWeight = all_bmi[key][0]
    fHeight = all_bmi[key][1]
    bmi = calculateSelectedUserBMI(intWeight, fHeight)
    return intWeight, fHeight, bmi


def calculateSelectedUserBMI(weight, height):
    bmi = round(weight / (height ** 2), 2)
    print(bmi)
    contOfSelectedUserBMI.set(bmi)
    contOfSelectedUserBMIClassification.set(entryBMIClassifcation(bmi))
    return bmi


# Data stored for use in the developed module.

lstNames = ['Reed',
            'Helena',
            'Lukas',
            'Tennyson',
            'Cyriacus',
            'Lubov']

all_bmi = {"reed": (106, 1.73),
           "helena": (74, 1.63),
           "lukas": (90, 1.80),
           "tennyson": (82, 1.77),
           "cyriacus": (98, 1.75),
           "lubov": (70, 1.54)}

# Welcome note that appears at the top of the window when the user starts the program.

contOfWelcome = StringVar()
contOfWelcome.set(WELCOME)
entWelcome = Entry(window, width=90, state="readonly", textvariable=contOfWelcome, font="Calibre 10")
entWelcome.grid(row=0, column=1, rowspan=4, columnspan=4, padx=(0, 0), pady=(15, 30), sticky=NSEW)

# First off, a list of names is displayed so that the user may a name and the BMI for a particular individual is
# displayed along with their corresponding BMI Classification.

yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=2, rowspan=4, column=1, padx=(0, 200), pady=(50, 50))

# As the list has been provided at the start of the document, it's not needed to be assigned again. The list will now
# be used to create a scroll menu for the user to select from.

conOflstNE = StringVar()
lstNE = Listbox(window, width=14, height=4, listvariable=conOflstNE, yscrollcommand=yscroll.set, font=FONT)
lstNE.grid(row=2, column=0, rowspan=4, padx=(10, 0), pady=(70, 50), stick=E)
conOflstNE.set(tuple(lstNames))
yscroll['command'] = lstNE.yview
lstNE.bind('<<ListboxSelect>>', selectUser)

# When the user selects a name from the listbox, the BMI calculation, classification, weight and height will show.
lblSelectedUserBMI = Label(window, text="BMI: ", font=FONT)
lblSelectedUserBMI.grid(row=5, column=0, padx=(40, 10), pady=(50, 0), sticky=W)

contOfSelectedUserBMI = StringVar()
entSelectedUserBMICalc = Entry(window, width=10, state="readonly", textvariable=contOfSelectedUserBMI)
entSelectedUserBMICalc.grid(row=5, column=1, padx=(5, 30), pady=(50, 0), sticky=W)

lblSelectedUserBMIClassification = Label(window, text="Classification: ", font=FONT)
lblSelectedUserBMIClassification.grid(row=6, column=0, padx=(40, 20), pady=(10, 0), sticky=E)

contOfSelectedUserBMIClassification = StringVar()
entSelectedUserBMIClassification = Entry(window, width=24, state="readonly",
                                         textvariable=contOfSelectedUserBMIClassification)
entSelectedUserBMIClassification.grid(row=6, column=1, padx=(5, 0), pady=(15, 10), sticky=W)


# Second: For new values, the user can provide a weight and height to be calculated. This is a 3 step process,
# outlined below.

# Step 1. Weight value provided by user
lblWeight = Label(window, text="Weight: ", font=FONT)
lblWeight.grid(row=4, column=3, padx=5, pady=0)
contOfWeight = StringVar()  # contents of the Entry widget for the Weight to be used to calculate.

entWeight = Entry(window, textvariable=contOfWeight, width=10)
entWeight.grid(row=4, column=4, padx=(0, 25), pady=0, sticky=W)
entWeight.insert(0, 'in kg')
entWeight.bind('<Button-1>', clearEntryWidgetWeight)

# Step 2. Height value provided by user
lblHeight = Label(window, text="Height: ", font=FONT)
lblHeight.grid(row=5, column=3, padx=(0, 0), pady=20, sticky=N)
contOfHeight = StringVar()  # contents of the Entry widget for the Height to be used to calculate.

entHeight = Entry(window, textvariable=contOfHeight, width=10)
entHeight.grid(row=5, column=4, padx=(0, 25), pady=20, sticky=NW)
entHeight.insert(0, 'in metres')
entHeight.bind('<Button-1>', clearEntryWidgetHeight)

# Step 3. After the user provides a weight and a height, the user clicks on 'calculate' to calculate the bmi value
btnCalculate = Button(window, text="Calculate", font=FONT, width=10,
                      command=lambda: entryBMICalculation(int(entWeight.get()), float(entHeight.get())))
btnCalculate.grid(row=8, column=3, padx=(0, 0), pady=(30, 0), sticky=N)

# The calculated value is displayed for the user. The calculated value and associated classification are both displayed
# in a readonly entry widget.
lblBMI = Label(window, text="BMI: ", font=FONT)
lblBMI.grid(row=6, column=3, padx=(5, 20), pady=(0, 0))

contOfBMI = StringVar()
entBMICalc = Entry(window, width=10, state="readonly", textvariable=contOfBMI)
entBMICalc.grid(row=6, column=4, padx=(5, 35), pady=(5, 0), sticky=W)

lblBMIClassification = Label(window, text="Classification: ", font=FONT)
lblBMIClassification.grid(row=7, column=3, padx=(46, 0), pady=(5, 0))

contOfBMIClassification = StringVar()
entBMIClassification = Entry(window, width=24, state="readonly", textvariable=contOfBMIClassification)
entBMIClassification.grid(row=7, column=4, padx=(0, 85), pady=(5, 0))


# Once the user has calculated the first BMI value, they have the option of clearing the entry widgets to calculate
# new values. Clicking on 'reset' will clear the values and prepare it for the next calculation.
clear = Button(window, text='Reset', command=btnReset, font=FONT, width=10)
clear.grid(row=8, column=4, padx=(0, 0), pady=(30, 0), sticky=N)

# NOTE: At any point in time, the user can exit the program by clicking on 'exit'
btnExit = Button(window, text="Exit", background="sky blue", font=FONT, command=window.destroy)
btnExit.grid(row=8, column=8, padx=(100, 10), pady=(120, 10), sticky=SW)

window.mainloop()
