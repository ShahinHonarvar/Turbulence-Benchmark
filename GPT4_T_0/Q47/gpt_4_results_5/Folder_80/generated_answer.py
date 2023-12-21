
def palindromes_of_specific_lengths(s):
    import re
    s = s[35:89]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+24, min(i+34, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[A-Za-z]*$", substring):
                palindromes.add(substring.lower())
    return palindromes
