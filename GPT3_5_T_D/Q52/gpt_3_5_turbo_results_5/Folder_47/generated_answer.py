
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindromes = set()
    
    for i in range(len(string)-33):
        substring = string[i:i+34]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
