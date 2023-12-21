
import re

def palindrome_of_length_n(string):
    length = 407
    palindromes = set()
    string = re.sub(r'[^a-zA-Z]', '', string)
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
