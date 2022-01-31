import sys

from Mad_Libs import *
a = Madlibs
def testit(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def check_input_test_suite():
    """
    checks if user input is valid
    :return:
    """
    testit(Madlibs.check_input("r", "r", "r", "r", "r") == False)
    # testit(Madlibs.check_input(() == True))


def main():

   check_input_test_suite()


if __name__ == "__main__":
    main()