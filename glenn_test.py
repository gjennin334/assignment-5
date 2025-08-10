"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message: borrow_book() public method completed

This is file "glenn_test.py" and contains my class test code.
here's my github repository, it is publicly readable:
    https://github.com/gjennin334/assignment-5.git

borrow_book() can pretty much call all the other things 
but it needs to return things:
(a) if no such book, invalid string etc, return -1
      all gettable attributes will return None
(b) if book exists but none available for checkout, return 0
      all gettable attributes will return valid data
(c) if checkout is successful, 
      all gettable attributes will return valid data


"""

# glenn_test.py
 
# import GlennClass          # this does not work with x = GlennClass()
from GlennClass import *     # but this does.

def attempt( my_lib, guess ):
    result = my_lib.borrow_book( guess )
    if result < 0:
        print(f"no such book as '{guess}'")
    else:                     # these two cases access a real book:
        print(f"book '{my_lib.get_title()}' by ",
              f"'{my_lib.get_author()}' ",
              f"(published {my_lib.get_publication_year()}) ", sep='',end='')
        if result == 0:
            print("is UNAVAILABLE")
        else:
            print("is YOURS now")

def main():
    # initialize the dictionary and other internal attributes:
    my_lib = GlennClass()
    # take a few pot-shots into the library:
    guess = "ry hug"
    # backlist = my_lib.search_by_title(guess)
    # print(f"guess '{guess}' yields: {backlist}")

    attempt( my_lib, guess )
    attempt( my_lib, guess )
    attempt( my_lib, guess )
    attempt( my_lib, "heit" )
        
if __name__ == "__main__":
    main()



