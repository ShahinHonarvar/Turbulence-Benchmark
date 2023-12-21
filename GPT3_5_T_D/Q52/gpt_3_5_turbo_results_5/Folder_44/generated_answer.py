
import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = r'(?=(\b[a-zA-Z]{445}\b))'
    matches = re.findall(pattern, string)
    if matches:
        return set(matches)
    else:
        return set()
