
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(string)):
        for j in range(i+94, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    
    return palindromes
