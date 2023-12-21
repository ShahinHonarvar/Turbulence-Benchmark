
import re

def palindromes_of_specific_lengths(string):
    substring = string[:6].lower()
    palindromes = set()
    for i in range(3, 6):
        for j in range(6-i+1):
            if re.match("^[a-zA-Z]+$", substring[j:j+i][::-1]):
                palindromes.add(substring[j:j+i])
    return palindromes
