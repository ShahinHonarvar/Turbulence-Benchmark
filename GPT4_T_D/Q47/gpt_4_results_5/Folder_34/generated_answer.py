
import re

def palindromes_of_specific_lengths(string):
    substr = string[200:301]
    palindromes = set()
    for i in range(10, 51):
        for j in range(len(substr) - i + 1):
            temp = substr[j:j+i]
            if temp.lower() == temp.lower()[::-1] and temp.isalpha():
                palindromes.add(temp.lower())
    return palindromes
