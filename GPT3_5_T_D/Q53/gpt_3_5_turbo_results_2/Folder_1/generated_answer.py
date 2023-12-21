
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub("[^a-zA-Z]", "", string)
    string = string.lower()
    
    def is_palindrome(s):
        return s == s[::-1]
    
    for i in range(len(string)):
        for j in range(i + 29, len(string) + 1):
            substr = string[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    
    return palindromes
