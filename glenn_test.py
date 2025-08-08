"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 8, 2025

Commit Message:  initial commit, my class and test skeletons

This is file "glenn_test.py" and contains my class test code.
It is meant to IMPORTED the second file "GlennTest.py"
where both files are in the same directory and the "current
directory" of the CLI is also in that same directory.

the result of executing "python glenn_test.py" with the files in this
first commit is:

    % python glenn_test.py
    you are in the __init_ for the class
    it's alive, it's alive

here's my github repository, it is publicly readable:

    https://github.com/gjennin334/assignment-5.git

it is cloned into VSCode and the first commit will be from there.

"""

# glenn_test.py
 
# import GlennClass          # this does not work with x = GlennClass()
from GlennClass import *     # but this does.

def main():
    new_glennclass = GlennClass()
    print("it's alive, it's alive")
    
if __name__ == "__main__":
    main()



