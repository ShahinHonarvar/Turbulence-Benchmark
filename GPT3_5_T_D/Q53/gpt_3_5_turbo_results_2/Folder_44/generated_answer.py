
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i+89, len(string)+1):
            word = string[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
