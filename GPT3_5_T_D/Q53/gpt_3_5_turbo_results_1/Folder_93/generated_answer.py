
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    
    letters = re.findall('[a-zA-Z]', string)
    letters = ''.join(letters).lower()
    
    for i in range(len(letters)):
        for j in range(i + 90, len(letters) + 1):
            if letters[i:j] == letters[i:j][::-1]:
                palindromes.add(letters[i:j])
    
    return palindromes
