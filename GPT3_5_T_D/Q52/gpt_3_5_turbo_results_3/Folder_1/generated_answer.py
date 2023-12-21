
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    pattern = r'[a-z]+'
    words = re.findall(pattern, string)

    for word in words:
        if len(word) == 27:
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
