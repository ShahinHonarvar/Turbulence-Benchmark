
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string).lower()
    length = len(string)
    palindromes = set()
    
    for i in range(length - 72):
        substring = string[i:i+73]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
