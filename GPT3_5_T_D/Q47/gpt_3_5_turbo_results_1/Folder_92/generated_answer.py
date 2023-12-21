
import re

def palindromes_of_specific_lengths(string):
    string = string[:5]
    palindromes = set()
    
    for i in range(len(string)-2):
        substring = string[i:i+3]
        if len(substring) == 3 and self._is_palindrome(substring):
            palindromes.add(substring)
            
        if i+4 <= len(string):
            substring = string[i:i+4]
            if len(substring) == 4 and self._is_palindrome(substring):
                palindromes.add(substring)
            
    return palindromes

def _is_palindrome(string):
    string = re.sub('[^a-zA-Z]+', '', string.lower())
    return string == string[::-1]
