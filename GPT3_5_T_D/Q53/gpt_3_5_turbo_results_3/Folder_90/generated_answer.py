
import re

def palindrome_of_length_at_least_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i+140, len(string)+1):
            substr = string[i:j]
            if re.match("^[a-zA-Z]+$", substr) and substr == substr[::-1]:
                result.add(substr)
    return result
