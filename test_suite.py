# Name- Paw Ehler Thaw, Alejandro Ramos
# Username- thawp, ramosa
#
# Assignment Number- P01
#
# Purpose: Here we implement a test suite to demonstrate testing of Boolean functions
#######################################################################
# Acknowledgements: Dr. Shepherd, Anish, Destiney, Ahmed, May, Chesky, Collins
#   Original Author: Jess Franken
#   Based on the Best Yo Mama Jokes:
#   https://bestlifeonline.com/yo-mama-jokes/
#######################################################################
# Repo Link- https://github.com/Berea-College-CSC-226/p01-ale-paw-final
# Google Docs - https://docs.google.com/document/d/1chVOIYBNiCezkGpYfTPnQu3ymoDrIn3Wq1dQvz1ECCg/edit?usp=sharing
#######################################################################

import sys
from Mad_Libs import*
TESTNUM = 1


def mytest( did_pass ):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    global TESTNUM

    if did_pass:
        msg = 'Test %d Passed' % TESTNUM
    else:
        msg = 'Test %d Failed' % TESTNUM
    print(msg)

    TESTNUM += 1


def input_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the check_input function.

    :return: None

    """
    print("\nRunning input_testsuite().")

    test = Madlibs()
# test correct inputs of (family type, adjective, object, time of day, food)
    mytest(test.check_input("grandpa", "fat", "chair", "noon", "pizza") == True)  # testing correct input
    mytest(test.check_input("grandma", "ugly", "phone", "morning", "lasagna") == True)  # testing correct input
    mytest(test.check_input("father", "hairy", "table", "night", "pie") == True)  # testing correct input
    mytest(test.check_input("Mom", "beautiful", "hat", "Dawn", "noodles") == True)  # testing correct input
    mytest(test.check_input("Sister", "hairy", "table", "evening", "ham") == True)  # testing correct input

    mytest(test.check_input("Mom", "pretty", "brick", "noon", "1008") == False)  # testing incorrect input
    mytest(test.check_input("%^*", "chubby", "", "ring", "()") == False)  # testing incorrect input
    mytest(test.check_input("", "fat", "chair", "", "9") == False)  # testing incorrect input
    mytest(test.check_input("*", "90", "phone", "", "lasagna") == False)  # testing incorrect input
    mytest(test.check_input("1", "hairy", "#$", "night", "gravy") == False)  # testing incorrect input

    mytest(test.check_input("", "", "", "", "") == False)  # testing incorrect input with empty strings
    mytest(test.check_input("90", "12", "12451", "8654", "25829") == False)  # testing incorrect input with numbers
    mytest(test.check_input("!", "*", "()", "&", "%") == False)  # testing incorrect input with special characters

    print("Run of input_testsuite() complete.")


def main():
    """
    This main function is intended to test the correctness of the check_input function

    :return: None
    """
    input_testsuite()   # call the test suite function that utilizes the testit()
    # function and is designed to test the check_input function.


if __name__ == "__main__":
    main()