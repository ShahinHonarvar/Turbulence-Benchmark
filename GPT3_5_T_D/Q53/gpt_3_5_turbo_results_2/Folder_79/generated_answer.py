
import re

def palindrome_of_length_at_least_n(string):
    result = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())
    length = len(string)
    
    for i in range(length):
        for j in range(i + 17, length + 1):
            substr = string[i:j]
            if substr == substr[::-1] and len(substr) >= 17:
                result.add(substr)
    
    return result
