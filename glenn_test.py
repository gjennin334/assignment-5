"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message:  search_by_title() public method completed

This is file "glenn_test.py" and contains my class test code.
here's my github repository, it is publicly readable:
    https://github.com/gjennin334/assignment-5.git

search_by_title() permits a customer with an incomplete knowledge
of a book title to get a list of candidate (correct, full) title strings.
an empty list might be returned.

"""

# glenn_test.py
 
# import GlennClass          # this does not work with x = GlennClass()
from GlennClass import *     # but this does.

def main():
    # initialize the dictionary and other internal attributes:
    my_lib = GlennClass()
    # take a few pot-shots into the library:
    guess = "r yhug"
    backlist = my_lib.search_by_title(guess)
    print(f"guess '{guess}' yields: {backlist}")
    
if __name__ == "__main__":
    main()



