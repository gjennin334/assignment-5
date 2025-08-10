"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message:  __init__dictionary and get/set methods

This is file "glenn_test.py" and contains my class test code.
here's my github repository, it is publicly readable:
    https://github.com/gjennin334/assignment-5.git

This commit tests the creation of the initial library dictionary at __init__
and its needed internal get/set methods


"""

# glenn_test.py
 
# import GlennClass          # this does not work with x = GlennClass()
from GlennClass import *     # but this does.

def main():
    new_glennclass = GlennClass()
    # initialize the dictionary and other internal attributes:
    print("it's alive, it's alive")
    
if __name__ == "__main__":
    main()



