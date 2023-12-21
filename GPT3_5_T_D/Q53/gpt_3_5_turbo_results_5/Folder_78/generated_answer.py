
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    results = set()
    
    for i in range(len(string)):
        for j in range(i+96, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                results.add(substring)
    
    return results
