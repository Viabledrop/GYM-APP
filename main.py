from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv

# SETUP
window = Tk()
window.geometry('520x540')
window.title("Fitness App")
window.configure(background='black')

# METHODS
def save():
    select = var.get()
    if (select == 0 or select == 1 or select == 2):
        if (excerciseInput.index('end') == 0):
            mb.showwarning('Missing details', 'enter your excercise name')
        elif (setInput.index('end') == 0):
            mb.showwarning('Missing details', 'enter your sets')
        elif (weightInput.index('end') == 0):
            mb.showwarning('Missing details', 'enter your weights')
        elif (repsInput.index('end') == 0):
            mb.showwarning('Missing details', 'enter your reps')
        else:
            mb.showinfo('Success', 'Sucesfully uploaded user data ')
    else:
        mb.showinfo("Missing details", 'enter an excercise type')
    # get from all the entries
    exType = var.get() # excercise type PPL
    dayofExcercise = dayInput.get_date().strftime('%d/%m/%Y') # day of week
    now = datetime.datetime.now()

    if exType == 0: PPLType = 'Push'
    elif exType == 1: PPLType = 'Pull'
    else: PPLType = 'Legs'

    stringData ='\n'+now.strftime("%d-%m-%Y %H:%M")+'\t' + dayofExcercise + '\t' +excerciseInput.get()+'\t'+PPLType+'\t'+setInput.get()+'\t'+ weightInput.get()+'\t'+repsInput.get()

    f = open(('regdetails.txt'), 'a')
    f.write(stringData)
    f.close()

    # save inside of csv file
    with open('Regfile.csv', 'a') as fs:
        w = csv.writer(fs, dialect='excel-tab')
        w.writerow([now.strftime("%d-%m-%Y %H:%M"), dayofExcercise,excerciseInput.get(), PPLType, setInput.get(), weightInput.get(), repsInput.get()])
        fs.close()

def msg():
    pass

def saveinfo():
    save()
    msg()

### elements ####
# title
title = Label(window, text="Exercise Form", width=25, font=("sanf serif", 20, "bold"), bg='red', fg='white')
title.place(x=70, y=50)

# DAY OF EXCERCISE
dayLabel = Label(window, text="Day:", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
dayInput = DateEntry(window, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
dayInput.place(x=240,y=130)
dayLabel.place(x=70,y=130)

# EXCERCISE NAME
excerciseNameLabel = Label(window, text="Excercise:", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
excerciseInput = Entry(window,width=30,bd=2)
excerciseInput.place(x=240,y=180)
excerciseNameLabel.place(x=70,y=180)

# TYPE OF EXCERCISE
var = IntVar()
excerciseType = Label(window, text="Type:", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
pushRadio = Radiobutton(window, text="Push", variable=var, value=0, font=("times",12),bg='red', fg='black')
pullRadio = Radiobutton(window, text="Pull", variable=var, value=1, font=("times",12),bg='red', fg='black')
legsRadio = Radiobutton(window, text="Legs", variable=var, value=2, font=("times",12),bg='red', fg='black')
excerciseType.place(x=70,y=230)
pushRadio.place(x=235,y=230)
pullRadio.place(x=315,y=230)
legsRadio.place(x=395,y=230)

# SET
setLabel = Label(window, text="Set(s):", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
setInput = Entry(window,width=30,bd=2)
setInput.place(x=240,y=280)
setLabel.place(x=70,y=280)

# Weights
weightLabel = Label(window, text="Weight Per Set:", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
weightInput = Entry(window,width=30,bd=2)
weightInput.place(x=240,y=330)
weightLabel.place(x=70,y=330)

# Reps
repsLabel = Label(window, text="Reps Per Set:", width=20, font=("times", 12, "bold"), anchor="w", bg='black', fg='white')
repsInput = Entry(window,width=30,bd=2)
repsInput.place(x=240,y=380)
repsLabel.place(x=70,y=380)

# SUBMIT & CANCEL
submitButton = Button(window, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
submitButton.place(x=120,y=440)
cancelButton = Button(window, text='Cancel',command=window.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
cancelButton.place(x=320,y=440)

window.mainloop()