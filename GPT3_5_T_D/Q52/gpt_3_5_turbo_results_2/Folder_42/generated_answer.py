
import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)-278):
        substring = s[i:i+279]
        if re.match('^[a-zA-Z]+$', substring):
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
