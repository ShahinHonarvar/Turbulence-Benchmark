
import re

def return_nth_smallest_ascii(strng):
    # Find all the characters in the given range
    # List comprehension
    char_list = [c for c in strng[4:-1]]
    # Sort the list by ASCII value
    char_list.sort()
    # Get the 4th smallest value
    return char_list[3]
