
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:83]
    substring = re.sub('[^A-Za-z]', '', substring)
    substring = substring.lower()
    palindromes = set()

    for i in range(len(substring) - 34):
        if substring[i:i+35] == substring[i:i+35][::-1]:
            palindromes.add(substring[i:i+35])

    return palindromes
