
import re

def palindrome_of_length_at_least_n(string):
    result = set()
    string = re.sub(r'[^a-zA-Z]', '', string)
    
    for i in range(len(string)-97):
        substring = string[i:i+98].lower()
        if substring == substring[::-1] and len(substring) >= 98:
            result.add(substring)
    
    return result
