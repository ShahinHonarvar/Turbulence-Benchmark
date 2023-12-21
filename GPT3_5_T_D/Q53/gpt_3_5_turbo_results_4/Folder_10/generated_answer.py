
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string)-91):
        for j in range(i+91, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
