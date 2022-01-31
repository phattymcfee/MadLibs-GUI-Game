import tkinter as tk
from tkinter import ttk

def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()
    print("hi")

HEIGHT = 200
WIDTH = 300

win = tk.Tk()  # Application Name
win.title("Python GUI App")  # Label
canvas = tk.Canvas(win, height=HEIGHT, width=WIDTH)

#CREATE BOARD

heading = ttk.Label(win, text = "Madlibs", font =("Times",75)).grid(row=0, column=0, columnspan=4, padx= 50)
lbl = ttk.Label(win, text="Enter the name:", font =("Times",25)).grid(column=0, row=1)  # Click event
vrb = ttk.Label(win, text="Enter the adjective:", font =("Times",25)).grid(column=0, row=2)  # Click event
non = ttk.Label(win, text="Enter the noun:", font =("Times",25)).grid(column=0, row=3)  # Click event
tim = ttk.Label(win, text="Enter the time:", font =("Times",25)).grid(column=0, row=4)  # Click event
fod = ttk.Label(win, text="Enter the food:", font =("Times",25)).grid(column=0, row=5)  # Click event
sen = ttk.Label(win, text="""Yo {0} is so {1} that they threw a {2} and it refused to come back until dinner\n at {3} where {4} was being served to celebrate the birth of the {0}.""",font =("Times",25)).grid(column=0, row=6)

#CLICK FUNCTION
def click():
    # print("Name:" + name.get())  # Textbox widget
    # print("Adjective:" + adjective.get())
    # print("Noun:" + noun.get())
    # print("Time:" + time.get())
    # print("Food:" + food.get())
    ttk.Label(win, text="hi" + "hi" + str(name.get())).grid(column=0, row=4)

name = tk.StringVar()
adjective = tk.StringVar()
noun = tk.StringVar()
time = tk.StringVar()
food = tk.StringVar()

#nameEntered = ttk.Entry(win, width=12, textvariable=name).grid(column=0, row=1)  # Button widget
nameEntered = ttk.Entry(win, width=12, textvariable=name).grid(column=1, row=1)  # Button widget
adjEntered = ttk.Entry(win, width=12, textvariable=adjective).grid(column=1, row=2)  # Button widget
nounEntered = ttk.Entry(win, width=12, textvariable=noun).grid(column=1, row=3)  # Button widget
timeEntered = ttk.Entry(win, width=12, textvariable=time).grid(column=1, row=4)
foodEntered = ttk.Entry(win, width=12, textvariable=food).grid(column=1, row=5)  # Button widget
#name
#FORMAT METHOD
# output = ("""Yo {0} is so {1} that they threw a {2} \n"""
#             """and it refused to come back until dinner\n"""
#             """at {3} where {4} was being served to celebrate the birth of the {0}.""".format(name, adjective, noun, time, food))


button = ttk.Button(win, text="submit", command=lambda: New_Window()).grid(column=0, row=7, columnspan= 4, padx = 25)




# w2 = tk.Label()
# w2.title("Second Screen")
# canvas = tk.Canvas(w2, height=HEIGHT, width=WIDTH)
# heading = ttk.Label(w2, text = "Madlibs", font =("Times",75)).grid(row=0, column=0, columnspan=4, padx= 50)



win.mainloop()