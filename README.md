# MadLibs GUI Game 

**Term**: Fall 2021 
️**Author(s)**: Alejandro Ramos, Paw Ehler Thaw

️indicates action items; you should remove these emoji as you complete/update the items which they accompany. (This means that your final README should have no ❗️in it!)

---

**References**: 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.
t07(Mad Libs), 
References - 
Dr. Shepherd - Dr. Shepherd helped us when we ran into an issue receiving user input and displaying the error boxes when it was invalid. 
May - May helped our program when we were having an issue with making the error boxes disappear after the user entered valid input after first inputting invalid input. 
Anish - Anish helped with our object oriented programming structure and test suite, specifically checking the check_input function. 
Destiney - Destiney was helpful in explaining the project. 
Collins - Collins helped with the logic of our test suite.

https://www.geeksforgeeks.org/python-grid-method-in-tkinter/ - This source helped us understand what .grid does and how to modify it.
https://docs.python.org/3/library/tkinter.html - This source provided documentation for the tkinter library and was a helpful reference.
https://pythonexamples.org/python-tkinter-button-change-font/ - This source helped us change the font for our program.
https://python-course.eu/tkinter_labels.php - This source has helped our understanding of labels in tkinter. 
https://pythonguides.com/python-tkinter-multiple-windows-tutorial/ - This source helped us understand how to create a new winder in tkinter. 
https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/ - This source has helped us visualize lambda in example code to better understand it.
https://riptutorial.com/tkinter/example/29713/grid-- - This source helped us recognize the various tools that can be used in the .grid method.
https://stackoverflow.com/questions/33046790/how-to-horizontally-center-a-widget-using-grid - We referenced this source to get an idea of how to center a grid widget.
https://stackoverflow.com/questions/47122132/how-to-validate-entry-in-tkinter - We used this source to understand how to get only alphabetical input from the user. (.isalpha)
https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python - This source helped us set the background color of our program. 
https://www.tutorialspoint.com/python/tk_fonts.htm - This source helped us look at the various fonts we can use in python.
https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter - This source helped us implement code that allowed us to get input from a user with tkinter. 
https://www.tutorialspoint.com/python/tk_text.htm - This source helped us recognize the various options and style designs for text in our program, specifically text color.
https://www.tutorialspoint.com/python/tk_relief.htm - This source was beneficial because it showed us the different relief styles that can be used with tkinter.
https://www.tutorialspoint.com/python/tk_button.htm - This source helped us implement code that allowed us to create a button that then created a new window. 
https://www.tutorialspoint.com/python/tk_grid.htm - This source helped us understand the various tools that can be used in .grid such as padx,pady,ipadx,ipady,sticky...
https://www.tutorialspoint.com/python/tk_pack.htm - This source helped us understand how to use .pack and the tools that accompany it suc as anchor, before, expand, side...
---


## Milestone 1: Setup, Planning, Design (1 Dec 2021)
️**Title**: What is the title of your project? 
MadLibs GUI Game
**Purpose**: In a single sentence, describe what your project will do.
The program will create a visual representation of the Madlibs program using gui tkinter instead.
️**Sources**: Which assignments or code will you base your project on?
We will base our project off of the t07-madlibs team assignment. 

️**CRC Card**:
  - Please write a CRC card for a class that your project will implement.
  - See this link for a sample CRC card and a template to
  use for your own cards (you will have to make a copy to edit): https://docs.google.com/document/d/15w42MZogoiMyctXsHYgEO0UCBlq91KrtVDFqtGx_6hU/edit#
  - Tables in markdown are not easy, so we suggest saving your CRC card
  as an image and including the image(s) in the README. You can do this
  by saving an image in the repository and linking to it. See the sample CRC card below - and replace it with your own.
  
  
<img width="430" alt="finalprojectcrs" src="https://user-images.githubusercontent.com/89230796/145504873-74cc4834-c914-4e85-98c9-5d659510d145.PNG">

---

## Milestone 2: Code (3 Dec 2021)

No README action items. You should have some code and a preliminary test suite pushed to your repository. 🙃

---

## Milestone 3: Virtual Check-In (6 Dec 2021)

Indicate what percentage of the project you have left to complete and how confident you feel. 

️**Completion Percentage**: 0 - 100%
We are about 80% complete. 

️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some strategies you can employ to increase the likelihood that you'll be successful in completing this project before the deadline.
We are not very confident. We are having doubts because as of right now, the program is not doing what we want it to do. When a user inputs a wrong
thing, it catches the error, but it does that and print the sentence out at the same time. We want it so that it first catches the error,
lets the user change their input, then once everything is correct it prints out the sentence. To increase the likelihood that we'll complete the project on time, we should go to 
the TA lab hours to get help and also reach out to Dr. Shepherd or Dr. Jan. 

---

## Milestone 4: Final Code, Presentation, Demo (10 Dec 2021)

### User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just   they hit the "Run" button. 

The user would first have to input a family type, an adjective, an object, the times of day, and a type of food.
Then they hit submit, if all the inputs are correct a sentence that includes their inputs should be printed. If their input is 
not correct (numbers/special characters) then it would raise an error.
<img width="323" alt="image" src="https://user-images.githubusercontent.com/89155580/153545710-4be31503-f7cf-4902-b981-093560e22e2f.png">

<img width="305" alt="image" src="https://user-images.githubusercontent.com/89155580/153545786-b7a845a9-f150-44f0-b9ed-b014c61b5c34.png">

<img width="694" alt="image" src="https://user-images.githubusercontent.com/89155580/153546048-f1bba3bf-7370-4cde-bdf5-ea704199ab4c.png">


### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.
* Because we use .isalpha(), the user can not input a " "(space) in the input. 
* We also could not center our main input window to the middle of the screen.(The first window that pops up)
* Another feature we would like to make aware is that because of the length of the family type error message, the entry boxes shift to the right whenever this type of error is created. 

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?

- What would you do differently next time, knowing what you know now?
- We chose the project Madlibs because we thought that it would be a good challenge for us as people who are new to coding.
We wanted a code that we really understood so that we can work with it and Madlibs was the perfect project to enhance since it
was simple and understandable. At the beginning we were about to base our project off the Game of Nim, but later on we decided 
to change it because the Game of Nim was for us, hard to understand. We know that it would be difficult to get it done on time given
our limited knowledge on tkinter and coding in general. The hardest part of this project was catching the user input's errors. It took a long time for us to find a solution to this. We tried many strageties,
and at the end we were able to find a solution. Our problem was that although the program did catch user error, sometimes it would still 
print the error message even though the user corrected their mistake. Sometimes the program would run fine, but on the fourth or fifth try, 
it would mess up. But with the help from a senior we were able to fix this problem by making a new method. Another difficult part was learning 
how to use the OOP along with tkinter. 

Our final project did reflect our original design. We based our ideas off Madlibs so it did what the original program did, but
we just added extra features to enhance it. In the original program, all the user inputs were done on the console and the 
sentence also printed out on the console. But with our new program we were able to use tkinter to make it look better. We got
the user input on a window and printed the sentence with the user input out on a different window. The difference is that 
this program catches user error while the original one does not. If a user inputs a number or a special character, it prints 
a error message and the message goes away when the user corrects their input. The second window will also not pop up until the
user's inputs are all correct. This program is also more interactive, so there are entry boxes where the user can type in their inputs
and then press the submit button. Last, but not least, this program has color! We changed the colors to light blue so that it would look
nice, but also not too much on the eyes.

Although we had to look almost everything up for this project, we did indeed learned a lot. We learned a bit more on how to use the
tkinter. We learned how to make entry boxes for the user inputs and also learned more on how to use the labels. We learned how to 
change the colors and sizes of letters, buttons, and labels. We also learned how to make a new window which was useful because it allowed us to implement the
program the way we wanted it run. We wanted the program to have more elements than just having everything in one window. So learning how to make the new window was very
helpful. During this process we learned more about the isalpha function which was really useful in catching user errors. 
Another big thing that we learned is the OOP. In the beginning we both had no clue as to how to use it and why it was more useful than the procedural, 
but now we have a better idea of how to use it. By coming to lab hours and asking others for help, we learned a lot. Knowing what we know now,
we would have first tried to understand how OOP worked because this was a big part of the project. I think that knowing it would
have made our project more smooth so that we can instead focus more on the tkinter part of it
