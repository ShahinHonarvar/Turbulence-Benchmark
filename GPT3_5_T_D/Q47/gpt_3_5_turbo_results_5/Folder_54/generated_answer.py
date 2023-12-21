
import re

def palindromes_of_specific_lengths(s):
    substring = s[27:78].lower()
    palindromes = set()
    for i in range(len(substring)-18):
        if len(substring[i:i+19]) > 19:
            break
        if re.match(r'^[a-zA-Z]+$', substring[i:i+19]) and substring[i:i+19] == substring[i:i+19][::-1]:
            palindromes.add(substring[i:i+19])
    return palindromes
