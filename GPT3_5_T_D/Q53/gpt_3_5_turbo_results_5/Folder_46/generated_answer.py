
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())
    
    for i in range(len(string) - 85):
        for j in range(i + 85, len(string)):
            substr = string[i:j+1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
