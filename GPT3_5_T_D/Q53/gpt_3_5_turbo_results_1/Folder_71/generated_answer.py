
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string) - 86):
        sub_string = string[i:i+87]
        reversed_sub_string = sub_string[::-1]
        
        if sub_string == reversed_sub_string:
            palindromes.add(sub_string)
    
    return palindromes
