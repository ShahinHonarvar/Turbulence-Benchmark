
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string).lower()
    palindromes = set()
    length = len(string)
    
    for i in range(length - 52):
        for j in range(i + 52, length):
            substring = string[i:j+1]
            if substring == substring[::-1] and len(substring) >= 53:
                palindromes.add(substring)
                
    return palindromes
