
import re

def return_nth_smallest_ascii(s):
    return next((char for char in re.findall(r"[A-Z]", s[18:-4]) if ord(char) == 19), None)
