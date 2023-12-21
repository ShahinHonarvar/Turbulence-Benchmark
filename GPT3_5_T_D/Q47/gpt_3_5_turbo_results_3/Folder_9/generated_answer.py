
import re

def palindromes_of_specific_lengths(string):
    pattern = r'[a-zA-Z]{50,60}'
    palindromes = set()
    for i in range(len(string)-59):
        substring = string[i:i+60]
        substring = re.sub('[^a-zA-Z]', '', substring)
        substring = substring.lower()
        if substring == substring[::-1] and len(substring) in range(50,61):
            palindromes.add(substring)
    return palindromes
