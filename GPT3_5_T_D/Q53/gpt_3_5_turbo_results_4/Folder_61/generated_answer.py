
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    
    for i in range(0, len(string)):
        for j in range(i+4, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
