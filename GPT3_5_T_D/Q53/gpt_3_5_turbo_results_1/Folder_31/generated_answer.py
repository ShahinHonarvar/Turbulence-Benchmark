
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+33, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                palindromes.add(string[i:j+1])
    
    return palindromes
