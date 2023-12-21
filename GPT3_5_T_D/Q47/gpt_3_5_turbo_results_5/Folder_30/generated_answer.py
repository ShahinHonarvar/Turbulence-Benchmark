
import re

def palindromes_of_specific_lengths(string):
    substring = string[14:91].lower()
    letters_only = re.sub("[^a-zA-Z]", "", substring)
    palindromes = set()
    
    for length in range(55, 72):
        for i in range(len(letters_only) - length + 1):
            substring = letters_only[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
