
import re

def palindromes_of_specific_lengths(string):
    string = string[:6]
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string)):
        for length in range(3, 6):
            if i + length > len(string):
                break
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
