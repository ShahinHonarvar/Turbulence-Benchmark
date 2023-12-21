
import re

def palindrome_of_length_at_least_n(word):
    word = re.sub("[^a-zA-Z]+", "", word).lower()
    palindromes = set()
    length = len(word)
    
    for i in range(length - 67 + 1):
        substring = word[i:i+67]
        
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
