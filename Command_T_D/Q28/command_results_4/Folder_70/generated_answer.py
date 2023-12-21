
import re

def return_nth_smallest_ascii(s):
    return next((a for a in s[28:-54] if ord(a) < ord(s[29])), s[28])
