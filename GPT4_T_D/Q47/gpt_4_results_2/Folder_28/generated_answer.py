
import re

def palindromes_of_specific_lengths(s):
    s = s[32:72].lower()
    palindromes_set = set()
    
    for i in range(len(s)):
        for j in range(i+21,min(i+33,len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[a-z]*$", substring):
                palindromes_set.add(substring)

    return palindromes_set
