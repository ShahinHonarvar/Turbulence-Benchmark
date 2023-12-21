
import re

def palindromes_of_specific_lengths(text):
    substring = text[32:80].lower()
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', sub):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes
