"""
Instructor: Edwin D. Sookiassian
CSIS 151 - Assignment 5: Class Creation
Name: Glenn Jennings    10281334
Date: August 10, 2025

Commit Message: borrow_book() public method completed

borrow_book() can pretty much call all the other things 
but it needs to return things:
(a) if no such book, invalid string etc, return -1
      all gettable attributes will return None
(b) if book exists but none available for checkout, return 0
      all gettable attributes will return valid data
(c) if checkout is successful, return 1 
      all gettable attributes will return valid data

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
        # print('initial dictionary is built:')
        # print( self._lib_inventory_ )

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

    def search_by_title( self, guess ):
        # print(f"search_by_title '{guess}'")
        result = []
        # get a normalized string, and it might be bad right off-the-bat:
        trial = self._normalize_the_title_(guess)
        if trial == None:
            return result                      # return an empty list
        # now we iterate over all the *keys* in our dictionary
        for book_key in self._lib_inventory_:
            # print(f"  iterating on key '{book_key}'")
            it_works = False
            if trial in book_key:
                # print(f"    '{trial}' IS a subset of '{book_key}'")
                it_works = True
            if not it_works:
                # let's squeeze any blanks out of both of the strings:
                squeezed = trial.replace(' ','')
                booksqueezed = book_key.replace(' ','')
                if squeezed in booksqueezed:
                    # print(f"    '{squeezed}' IS a subset of '{book_key}'")
                    it_works = True
            if it_works:    # we can add this to our output list.
                book_data = self._lib_inventory_.get(book_key)
                result.append(book_data[0])  # entry 0 is the correct title
        return result

    def _set_title_( self, to_become ):
        self._title_ = to_become
        
    def _set_author_( self, to_become ):
        self._author_ = to_become

    def _set_publication_year_( self, to_become ):
        self._publication_year_ = to_become

    def _set_copies_available_( self, to_become ):
        self._copies_available_ = to_become

    def _set_copies_checked_out_( self, to_become ):
        self._copies_checked_out_ = to_become


    def get_title( self ):
        if not self._valid_entry_:
            return None
        return self._title_
        
    def get_author( self ):
        if not self._valid_entry_:
            return None
        return self._author_

    def get_publication_year( self ):
        if not self._valid_entry_:
            return None
        return self._publication_year_

    def get_copies_available( self ):
        if not self._valid_entry_:
            return None
        return self._copies_available_

    def get_copies_checked_out( self ):
        if not self._valid_entry_:
            return None
        return self._copies_checked_out_


    def borrow_book( self, guess ):
        self._valid_entry_ = False
        # get a normalized string, and it might be bad right off-the-bat:
        trial = self._normalize_the_title_(guess)
        if trial == None:
            return -1                           # return a no-such-book
        # we do an abbreviated variant of "search_by_title":
        result = []
        # now we iterate over all the *keys* in our dictionary
        for book_key in self._lib_inventory_:
            # print(f"  iterating on key '{book_key}'")
            it_works = False
            ### I think this subset is BAD  it might cause a book to be masked
            if trial in book_key:
                result.append(book_key)  # we want the normalized key here
        # there must be exactly one result, a unique book.
        if len(result) != 1:
            return -1                           # return a no-such-book
        dict_key = result[0]         # needed to access the data.
        book_data = self._lib_inventory_.get(dict_key)  # now we have data.
        self._valid_entry_ = True    # no get/set for this foudational.
        print('BOOK DATA NOW:',book_data)
        self._set_title_(              book_data[0] )
        self._set_author_(             book_data[1] )
        self._set_publication_year_(   book_data[2] )
        self._set_copies_available_(   book_data[3] )
        self._set_copies_checked_out_( book_data[4] )
        # so what do we tell the customer ?
        if self._copies_available_ <= 0:
            return 0                 # return a yes-book but none available
        # check it out,
        # update the gettable attributes,
        self._set_copies_available_(   self._copies_available_   - 1 )
        self._set_copies_checked_out_( self._copies_checked_out_ + 1 )
        # and update the dictionary.  do NOT use "get" here !!!
        self._lib_inventory_[dict_key] = \
            (self._title_, self._author_, self._publication_year_, \
             self._copies_available_, self._copies_checked_out_)
        return 1                     # successful checkout.
