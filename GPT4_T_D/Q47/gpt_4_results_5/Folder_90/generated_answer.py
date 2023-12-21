
import re

def palindromes_of_specific_lengths(string):
    substring = string[106:281]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+136, i+152):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate == candidate[::-1] and re.fullmatch("[A-Za-z]*", candidate):
                    palindromes.add(candidate.lower())
    return palindromes
