
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    size = 475
    result = set()
    for i in range(len(string) - size + 1):
        substr = string[i:i+size]
        substr_lower = substr.lower()
        if substr_lower == substr_lower[::-1]:
            result.add(substr)
    return result
