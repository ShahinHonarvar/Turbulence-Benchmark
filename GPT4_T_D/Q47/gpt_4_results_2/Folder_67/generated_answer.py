
import re 

def palindromes_of_specific_lengths(s):
    s = s[65:100]
    s = re.sub("[^a-zA-Z]", "", s)
    palindromes = set()

    for length in range(26, 34):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start+length]
            if substring.casefold() == substring[::-1].casefold():
                palindromes.add(substring)
                
    return palindromes
