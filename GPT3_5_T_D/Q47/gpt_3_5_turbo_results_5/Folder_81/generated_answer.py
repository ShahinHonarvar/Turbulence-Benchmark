
import string

def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[12:123]
    palindromes = set()
    for l in range(12, 221):
        for i in range(len(s) - l):
            if s[i:i+l] == s[i:i+l][::-1] and set(s[i:i+l]).issubset(string.ascii_lowercase):
                palindromes.add(s[i:i+l])
    return palindromes
