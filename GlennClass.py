"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message:   __init__dictionary and get/set methods

This commit tests the creation of the initial library dictionary at __init__
and its needed internal get/set methods

"""

class GlennClass:

    # there are two principle attributes
    #  _lib_inventory_    initialized to the library's contents
    #  _valid_entry_      initialized to False
    # and when accessed with a valid key, these additional
    # attributes become defined:
    #  _valid_entry_ is set to True
    #  _title_
    #  _author_
    #  _publication_year_
    #  _copies_available_
    #  _copies_checked_out_
    # I have defined these with _x_ as they are meant to be hidden.

    def __init__(self):
        self._lib_inventory_ = {}      # a dictionary
        self._valid_entry_ = False
        self._title_ = None
        self._author_ = None
        self._publication_year_ = None
        self._copies_available_ = None
        self._copies_checked_out_ = None
        # 
        # this init sequence is assumed error-free.  have to start somewhere.
        # using the "direct assignment" method to build the dictioary.
        #
        nomn = self._normalize_the_title_("Henry Huggins")
        datatuple = ("Henry Huggins", "Beverly Cleary", 1950, 2, 0)
        self._lib_inventory_[nomn] = datatuple
        #
        nomn = self._normalize_the_title_("Fahrenheit 451")
        datatuple = ("Fahrenheit 451", "Ray Bradbury", 1953, 0, 1 )
        self._lib_inventory_[nomn] = datatuple
        print('initial dictionary is built:')
        print( self._lib_inventory_ )

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
        stage_two = stage_one.replace('\t',' ') # tabs to spaces
        stage_three = " ".join(stage_two.split()) # combine multiple spaces
        stage_four = stage_three.lower()          # downshift all alphas
        if stage_four == '':                    # eliminate empty strings
            print(f" ** '{in_name}' is invalid")
            return None
        if not any(kar.isalpha() for kar in stage_four):  # at least one alpha
            # stage_four is an iterable, a list of characters.
            print(f" ** '{in_name}' is invalid")
            return None
        return stage_four



            
