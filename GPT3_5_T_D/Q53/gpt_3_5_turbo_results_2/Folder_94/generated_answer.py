
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    result = set()
    n = len(string)
    for i in range(n):
        for j in range(41, n - i + 1):
            substr = string[i:i + j]
            if substr == substr[::-1]:
                result.add(substr)
    return result
