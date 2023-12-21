
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:101]
    substring = re.sub('[^a-zA-Z]', '', substring).lower()
    palindromes = set()
    for i in range(10, 51):
        for j in range(len(substring) - i + 1):
            if substring[j:j+i] == substring[j:j+i][::-1]:
                palindromes.add(substring[j:j+i])
    return palindromes
