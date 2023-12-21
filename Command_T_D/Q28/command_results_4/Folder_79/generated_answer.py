
import re

def return_nth_smallest_ascii(s):
    return next(char for i, char in enumerate(re.findall(r'[a-z]', s)) if ord(char) < ord(s[13]) and ord(char) > ord(s[35]))
