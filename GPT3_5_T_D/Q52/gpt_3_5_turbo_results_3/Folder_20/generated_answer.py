
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)-52):
        substring = string[i:i+53]
        substring = re.sub(r'[^a-zA-Z]', '', substring)
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes
