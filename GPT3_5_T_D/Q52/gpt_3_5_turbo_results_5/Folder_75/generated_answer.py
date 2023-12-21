
import re

def palindrome_of_length_n(s):
    substrings = set()
    length = 80
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if re.match('^[a-zA-Z]+$', substring):
            lowercase_substring = substring.lower()
            if lowercase_substring == lowercase_substring[::-1]:
                substrings.add(substring)
    return substrings
