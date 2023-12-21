
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^A-Za-z]', '', string.lower())
    
    for i in range(len(string)):
        for j in range(i+86, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
