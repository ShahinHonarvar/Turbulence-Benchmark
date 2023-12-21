
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W', '', s).lower()
    palindromes = set()
    for length in range(19, len(s) + 1):
        for i in range(len(s) - length + 1):
            slice = s[i:i+length]
            if slice == slice[::-1]:
                palindromes.add(slice)
    return palindromes
