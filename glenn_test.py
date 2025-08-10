"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message:  _normalize_the_title_() completed

This is file "glenn_test.py" and contains my class test code.
here's my github repository, it is publicly readable:
    https://github.com/gjennin334/assignment-5.git

This commit tests a private string-massaging method called
"_normalize_the_title_"

"""

# glenn_test.py
 
# import GlennClass          # this does not work with x = GlennClass()
from GlennClass import *     # but this does.

def main():
    new_glennclass = GlennClass()
    print("it's alive, it's alive")

    new_glennclass._normalize_the_title_("good")
    # new_glennclass._normalize_the_title_(None)
    # new_glennclass._normalize_the_title_(["a","b"])
    new_glennclass._normalize_the_title_(" Pre\tbonk ")
    new_glennclass._normalize_the_title_("  ")
    new_glennclass._normalize_the_title_(" 14 31 ")
    new_glennclass._normalize_the_title_("duo  Duo")
    
if __name__ == "__main__":
    main()



