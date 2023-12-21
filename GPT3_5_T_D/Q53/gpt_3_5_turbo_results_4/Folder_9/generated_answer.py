
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(string) - 94):
        for j in range(95, len(string) - i + 1):
            substring = string[i:i+j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
