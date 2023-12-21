
import re

def palindromes_of_specific_lengths(string):
    set_of_palindromes = set()
    substring = string[1:300].lower()

    for length in range(3, 11):
        for i in range(len(substring) - length + 1):
            substring_p = substring[i:i+length]
            if re.match('^[a-zA-Z]+$', substring_p) and substring_p == substring_p[::-1]:
                set_of_palindromes.add(substring_p)

    return set_of_palindromes
