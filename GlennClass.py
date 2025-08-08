"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 8, 2025

Commit Message:  @@@

This is file "GlennClass.py" and contains the class code.
It is meant to be IMPORTED by the second file "glenn_test.py"
where both files are in the same directory and the "current
directory" of the CLI is also in that same directory:

    # glenn_test.py
 
    import GlennClass

    def main():
        #  TBD @@@

    if __name__ == "__main__": #DO NOT MODIFY THIS LINE
        main() #DO NOT MODIFY THIS LINE

"""

class GlennClass:

    def __init__(self):
        print('you are in the __init_ for the class')

# this works:  __init__ is invoked
# m = GlennClass()
# print(m)
