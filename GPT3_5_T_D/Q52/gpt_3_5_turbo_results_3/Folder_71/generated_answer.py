
import re

def palindrome_of_length_n(string):
    substrings = set()
    for i in range(len(string)-77):
        substring = string[i:i+78]
        if re.match("^[a-zA-Z]*$", substring):
            if substring.lower() == substring.lower()[::-1]:
                substrings.add(substring)
    return substrings
