"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message:   _normalize_the_title_() completed

This commit implements a private string-massaging method called
"_normalize_the_title_" which takes the incoming string and returns 
a normalized string suitable to become a dictionary key.  If it
returns "None" then the string is rejected.

"""

class GlennClass:

    def __init__(self):
        print('you are in the __init_ for the class')

# internal method to massage an arbitrary string into a string
# suitable as a dictionary key:
# it will produce a lowercase string, cleaned-up regarding spaces
# that is: no lead or trail spaces, and only single spaces between "words"
# return "None" if input string is unacceptable or invalid

    def _normalize_the_title_( self, in_name ):
        isgood = False
        try:
            if isinstance( in_name, str ):   # is it a simple string ?
                isgood = True
        except Exception as e:
            pass
        if not isgood:
            print(f" ** {in_name} is invalid")
            return None
        # now clean up that string.  we might still get an empty string.
        stage_one = in_name.strip()             # lead and trail alank removal
        print(f"'{stage_one}' is OK so far")
        stage_two = stage_one.replace('\t',' ') # tabs to spaces
        print(f"'{stage_two}' is OK so far")
        stage_three = " ".join(stage_two.split()) # combine multiple spaces
        print(f"'{stage_three}' is OK so far")
        stage_four = stage_three.lower()          # downshift all alphas
        print(f"'{stage_four}' is OK so far")
        if stage_four == '':                    # eliminate empty strings
            print(f" ** '{in_name}' is invalid")
            return None
        if not any(kar.isalpha() for kar in stage_four):  # at least one alpha
            # stage_four is an iterable, a list of characters.
            print(f" ** '{in_name}' is invalid")
            return None
        return stage_four



            
