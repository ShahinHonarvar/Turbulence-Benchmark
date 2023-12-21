
import re

def palindrome_of_length_at_least_n(string):
    result = set()
    n = 66
    
    string = re.sub(r'[^A-Za-z]', '', string)
    string = string.lower()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            result.add(substring)
            
    return result
