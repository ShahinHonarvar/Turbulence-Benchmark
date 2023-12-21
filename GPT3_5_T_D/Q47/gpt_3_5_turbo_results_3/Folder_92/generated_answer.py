
import re

def palindromes_of_specific_lengths(string):
    result = set()
    for i in [3, 4]:
        for start in range(5 - i):
            substr = string[start:start + i]
            if re.match(r'^[a-zA-Z]+$', substr):
                substr = substr.lower()
                if substr == substr[::-1]:
                    result.add(substr)
    return result
