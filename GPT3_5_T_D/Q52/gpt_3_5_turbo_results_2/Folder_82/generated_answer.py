
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    n = 28
    if len(string) < n:
        return set()
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring.lower() == substring.lower()[::-1]:
            result.add(substring)
    return result
