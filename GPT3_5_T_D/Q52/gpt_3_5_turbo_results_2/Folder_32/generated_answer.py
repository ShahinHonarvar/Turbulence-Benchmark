
import re

def palindrome_of_length_n(s):
    substrings = set()
    s = s.lower()
    for i in range(len(s) - 112):
        substring = s[i:i+113]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                substrings.add(substring)
    return substrings
