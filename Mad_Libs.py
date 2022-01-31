#Name- Paw Ehler Thaw, Alejandro Ramos
#Username- thawp, ramosa
#
#Assignment Number- P01
#
#Purpose: Recreate out Madlibs program using GUI Tkinter
#######################################################################
# Acknowledgements: Dr. Shepherd, Anish, Destiney, Ahmed, May, Chesky, Collins
#   Original Author: Jess Franken
#   Based on the Best Yo Mama Jokes:
#   https://bestlifeonline.com/yo-mama-jokes/
#######################################################################
#Repo Link- https://github.com/Berea-College-CSC-226/p01-ale-paw-final
#Google Docs - https://docs.google.com/document/d/1chVOIYBNiCezkGpYfTPnQu3ymoDrIn3Wq1dQvz1ECCg/edit?usp=sharing
#######################################################################

import tkinter as tk
from tkinter import ttk

class Madlibs:
    '''
    The MadLibs class takes the user input and output it into a sentence. Along the way, it makes sure that the user only input
    letters and raise an error if they do not.
    '''
    def __init__(self):
        '''
        Initializer method a.k.a. Constructor
        '''
        self.win = tk.Tk()  # Application Name
        self.win.title("Madlibs GUI")
        self.win.configure(bg='lightblue')

        self.fam_type = tk.StringVar()  #makes sure self.fam_type is a string
        self.adj = tk.StringVar()       #makes sure self.adj is a string
        self.obj = tk.StringVar()       #makes sure self.obj is a string
        self.time = tk.StringVar()      #makes sure self.time is a string
        self.food = tk.StringVar()      #makes sure self.food is a string

        self.family_Type = ttk.Entry(self.win, width=12, textvariable=self.fam_type)      #where user can input a family type
        self.family_Type.grid(column=1, row=1)  # Button widget

        self.adjective = ttk.Entry(self.win , width=12, textvariable=self.adj)           #where user can input a adjective
        self.adjective.grid(column=1, row=2)  # Button widget

        self.object = ttk.Entry(self.win , width=12, textvariable=self.obj)               #where user can input a object
        self.object.grid(column=1, row=3)  # Button widget

        self.Time = ttk.Entry(self.win , width=12, textvariable=self.time)               #where user can input a time of day
        self.Time.grid(column=1, row=4)  # Button widget

        self.Food = ttk.Entry(self.win , width=12, textvariable=self.food)               #where user can input a type of food
        self.Food.grid(column=1, row=5)  # Button widget

        self.FAM_error = None    #sets the FAM_error to none
        self.ADJ_error = None    #sets the ADJ_error to none
        self.OBJ_error = None    #sets the OBJ_error to none
        self.TIME_error = None   #sets the Time_error to none
        self.FOOD_error = None   #sets the FOOD_error to none

        #the submit button first checks if user input is valid, then prints the sentence out on a new window if it is
        button = ttk.Button(self.win , text="submit",command=lambda:self.check_both()).grid(column=0, row=11, columnspan=1, pady = 5)

    def create_board(self):
        '''
        Creates the board that includes the heading and the label for fam_type, adj, obj, time, and food
        :return: None
        '''
        self.heading = ttk.Label(self.win, text="Madlibs",background = "lightblue", foreground = "black", font=("Times", 75)).grid(column=0,row=0, columnspan=4, padx=50, pady=20, sticky="nsew")
        self.fam_type = ttk.Label(self.win, text="Enter a family title:",background = "lightblue",foreground = "black", font=("Times", 25)).grid(column=0, row=1, sticky = "nsew", pady=7)  # Click event
        self.adj = ttk.Label(self.win, text="Enter a adjective:",background = "lightblue", foreground = "black", font=("Times", 25)).grid(column=0, row=2, sticky = "nsew", pady=7)  # Click event
        self.obj = ttk.Label(self.win, text="Enter a object:",background = "lightblue", foreground = "black", font=("Times", 25)).grid(column=0, row=3, sticky ="nsew", pady=7)  # Click event
        self.time = ttk.Label(self.win, text="Enter a time of day:",background = "lightblue", foreground = "black", font=("Times", 25)).grid(column=0, row=4, sticky ="nsew", pady=7)  # Click event
        self.food = ttk.Label(self.win, text="Enter a food:", background = "lightblue", foreground = "black", font=("Times", 25)).grid(column=0, row=5, sticky ="nsew", pady=7)

    def remove_error(self, error):
        '''
        Removes the error display after inputing an invalid input
        :param error:
        :return:
        '''
        error.grid_forget()       #removes the error displays
        error = None

    def check_input(self, FAM, ADJ, OBJ, TIME, FOOD):
        '''
        Checks whether the user input is valid or not
        :param FAM: family type
        :param ADJ: a adjective
        :param OBJ: an object
        :param TIME: time of day
        :param FOOD: type of food
        :return: checker
        '''
        checker = True

        if self.FAM_error is not None:                       #initially forgets the error messages
            self.remove_error(self.FAM_error)
        if not FAM.isalpha():                                #checks if user input of family type are all letters
            self.FAM_error = ttk.Label(self.win , text="ENTER VALID FAMILY TITLE", background="lightblue", foreground="red", font=("Times", 15))
            self.FAM_error.grid(column=0, row=6, pady=5)
            checker = False
        else:                                                #if the user's input for family type is correct it forgets it
            if self.FAM_error is not None:
                self.FAM_error.grid_forget()
                self.FAM_error = None

        if self.ADJ_error is not None:                       #initially forgets the error messages
            self.remove_error(self.ADJ_error)
        if not ADJ.isalpha():                                #checks if user input of adjective are all letters
            self.ADJ_error = ttk.Label(self.win , text="ENTER VALID ADJECTIVE",background="lightblue", foreground="red", font=("Times", 15))
            self.ADJ_error.grid(column=0, row=7,pady=5)
            checker = False

        else:
            if self.ADJ_error is not None:                   #if the user's input for adj is correct it forgets it
                self.ADJ_error.grid_forget()
                self.ADJ_error = None

        if self.OBJ_error is not None:                       #initially forgets the error messages
            self.remove_error(self.OBJ_error)
        if not OBJ.isalpha():                                #checks if user input of object are all letters
            self.OBJ_error = ttk.Label(self.win , text="ENTER VALID OBJECT", background="lightblue", foreground="red",font=("Times", 15))
            self.OBJ_error.grid(column=0, row=8,pady=5)
            checker = False

        else:
            if self.OBJ_error is not None:
                self.OBJ_error.grid_forget()        #if the user's input for obj is correct it forgets it
                self.OBJ_error = None

        if self.TIME_error is not None:                #initially forgets the error messages
            self.remove_error(self.TIME_error)
        if not TIME.isalpha():                         #checks if user input of time of day are all letters
            self.TIME_error = ttk.Label(self.win , text="ENTER VALID TIME",background="lightblue", foreground="red", font=("Times", 15))
            self.TIME_error.grid(column=0, row=9,pady=5)
            checker = False

        else:
            if self.TIME_error is not None:
                self.TIME_error.grid_forget()          #if the user's input for time of day is correct it forgets it
                self.TIME_error = None

        if self.FOOD_error is not None:                #initially forgets the error messages
            self.remove_error(self.FOOD_error)
        if not FOOD.isalpha():                         #checks if user input of food are all letters
            self.FOOD_error = ttk.Label(self.win, text="ENTER VALID FOOD",background="lightblue", foreground="red",font=("Times", 15))
            self.FOOD_error.grid(column=0, row=10,pady=5)
            checker = False

        else:
            if self.FOOD_error is not None:
                self.FOOD_error.grid_forget()         #if the user's input for food is correct it forgets it
                self.FOOD_error = None
        return checker


    def check_both(self):
        '''
        This function first runs the check_input to make sure all the user inputs are valid. If all the inputs are valid, it then runs
        the New_Window function that prints the sentence.
        :return: None
        '''
        if (self.check_input(self.family_Type.get(), self.adjective.get(), self.object.get(), self.Time.get(), self.Food.get()) == True):
            self.New_Window()


    def New_Window(self):
        '''
        The new window that includes the sentence with user inputs and pops up when all user inputs are correct
        :return: None
        '''
        newWindow = tk.Toplevel(self.win) #create a window on top of the first window
        newWindow.geometry("700x300")  #sets the size of the window
        newWindow.configure(bg="lightblue") #change background color of new window to blue
        sentence = tk.Label(newWindow,text=("Yo " + self.family_Type.get() + " is so " + self.adjective.get() + ", that they threw a " + self.object.get() + " \n"
                            " and it refused to come back until a meal at " + self.Time.get() + ", where " + self.Food.get() + " \n"
                            " was being served to celebrate the birth of yo " + self.adjective.get() + " " + self.family_Type.get() +"!"),
                            background=("lightblue"),foreground = "black", font=("Times", 25))    #the sentence with user inputs
        heading_1 = tk.Label(newWindow, text=("Story"), background=("lightblue"), foreground="black",font=("Times", 75))
        heading_1.pack(side="top", padx=50, pady=20, anchor = "n")
        sentence.pack()        #packs widgets in rows and columns
        heading_1.pack()





def main():

    M = Madlibs()
    M.create_board()
    M.win.mainloop()

if __name__ == "__main__":
    main()