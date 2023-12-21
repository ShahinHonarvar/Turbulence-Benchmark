
import re

def return_nth_smallest_ascii(s):
    return next((x for x in s[51:-1] if x.isalpha()), 'z')
