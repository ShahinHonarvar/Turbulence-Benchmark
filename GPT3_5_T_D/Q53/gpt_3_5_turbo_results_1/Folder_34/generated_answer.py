
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^A-Za-z]', '', string.lower())
    length = len(string)
    
    for i in range(length):
        for j in range(i+68, length+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
