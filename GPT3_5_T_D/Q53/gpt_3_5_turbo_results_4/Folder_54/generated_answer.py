
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    
    for i in range(len(string) - 73):
        substring = string[i:i+74]
        substring = re.sub('[^a-zA-Z]', '', substring)
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    
    return palindromes
