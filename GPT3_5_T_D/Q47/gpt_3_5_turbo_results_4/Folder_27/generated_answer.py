
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[13:100]
    palindromes = set()

    for i in range(len(substring)-26):
        substring_26 = substring[i:i+26]
        substring_29 = substring[i:i+29]
        if re.match(r'^[a-zA-Z]+$', substring_26) and substring_26 == substring_26[::-1]:
            palindromes.add(substring_26)
        if re.match(r'^[a-zA-Z]+$', substring_29) and substring_29 == substring_29[::-1]:
            palindromes.add(substring_29)

    return palindromes
