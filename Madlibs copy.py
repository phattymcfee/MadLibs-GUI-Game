#Name- Paw Ehler Thaw, Alejandro Ramos
#Username- thawp, ramosa
#
#Assignment Number- T07
#Purpose: Gain practice using strings, additional practice breaking a larger problem down into smaller "pieces" using functions
#######################################################################
# Acknowledgements:
#   Original Author: Jess Franken
#   Based on the Best Yo Mama Jokes:
#   https://bestlifeonline.com/yo-mama-jokes/
#######################################################################
#Repo Link- https://github.com/Berea-College-CSC-226/t07-madlibs-paw-alejandro-t07
#Google Docs-https://docs.google.com/document/d/1OvaHRMd60hYFdBEWmR5EWJTV8ozobbAjP1tfa74DBUo/edit?usp=sharing
#######################################################################
def main():
    '''Main function that runs the code

    :Param: None
    :Return: None
    '''

    fam_member = input("Please enter family member type:")#create variables that store the type of input from the user
    adj = input("Please enter a adjective:")
    noun_two = input("Please enter a noun:")
    time = input("Please enter time of day:")
    food = input("Please enter a food:")
    print("""Yo {0} is so {1} that they threw a {2} \n"""
            """and it refused to come back until dinner\n"""
            """at {3} where {4} was being served to celebrate the birth of the {0}.""".format(fam_member, adj, noun_two, time, food)) # use the .format in order to call each input in the story
main()