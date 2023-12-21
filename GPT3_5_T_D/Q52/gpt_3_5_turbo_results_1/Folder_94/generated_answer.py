
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    n = 93
    palindromes = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    
    return palindromes
