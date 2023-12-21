
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    n = 76
    palindromes = set()
    
    for i in range(len(string) - n + 1):
        sub_string = string[i:i+n]
        if sub_string.lower() == sub_string.lower()[::-1]:
            palindromes.add(sub_string)
    
    return palindromes
