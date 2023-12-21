
import re

def return_nth_smallest_ascii(s):
    return next((char for i, char in enumerate(re.findall(r"[A-Z]", s[5:-2]) if i == 13), ""), s[0])
