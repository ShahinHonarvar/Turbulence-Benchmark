
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string.lower())
    palindromes = set()
    
    for i in range(len(string) - 29):
        for j in range(i + 29, len(string) + 1):
            text = string[i:j]
            if text == text[::-1]:
                palindromes.add(text)
    
    return palindromes
