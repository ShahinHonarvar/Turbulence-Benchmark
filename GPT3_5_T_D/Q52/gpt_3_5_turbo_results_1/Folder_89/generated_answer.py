
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)-37+1):
        substring = string[i:i+37]
        if re.search(r'(?i)^[a-z]+$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
