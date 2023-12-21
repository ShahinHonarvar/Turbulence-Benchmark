
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string)
    string = string.lower()
    palindromes = set()
    length = len(string)
    
    for i in range(length - 47):
        for j in range(48, min(length - i + 1, 49)):
            substring = string[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
