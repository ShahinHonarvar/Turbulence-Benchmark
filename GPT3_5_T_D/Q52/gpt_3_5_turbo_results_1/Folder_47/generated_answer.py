
import re

def palindrome_of_length_n(string):
    result = set()
    
    normalized_string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(normalized_string) - 33):
        substr = normalized_string[i:i+34]
        if substr == substr[::-1]:
            result.add(substr)
    
    return result
