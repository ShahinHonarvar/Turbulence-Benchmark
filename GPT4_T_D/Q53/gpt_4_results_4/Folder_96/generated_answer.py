
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = re.sub(r'\W+', '', string)
    
    palindromes = set()
    
    for len_sub in range(24, len(string) + 1):
        for i in range(0, len(string) - len_sub + 1):
            sub = string[i:i + len_sub]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
