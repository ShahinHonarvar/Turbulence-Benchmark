
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string).lower()
    result = set()
    for i in range(len(string) - 40):
        substr = string[i:i+41]
        if substr == substr[::-1]:
            result.add(substr)
    return result
