
import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile(r'[a-zA-Z]+')
    matches = re.findall(pattern, string)
    
    for word in matches:
        word = word.lower()
        for i in range(len(word) - 75):
            sub = word[i:i+76]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
