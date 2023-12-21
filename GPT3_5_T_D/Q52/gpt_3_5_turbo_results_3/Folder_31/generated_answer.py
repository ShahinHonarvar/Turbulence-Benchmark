
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    palindromes = set()
    
    for i in range(len(string) - 65):
        substring = string[i:i+66].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
