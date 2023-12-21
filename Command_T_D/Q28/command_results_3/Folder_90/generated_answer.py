
import re

def return_nth_smallest_ascii(strng):
    return next((c for c in strng[17:83] if ord(c) < 5), None)
