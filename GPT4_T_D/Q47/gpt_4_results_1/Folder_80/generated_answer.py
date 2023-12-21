
def palindromes_of_specific_lengths(s):
    import re
    substring = s[35:89]
    palindromes = set()
    for l in range(24, 34):
        for i in range(len(substring) - l + 1):
            sub = substring[i:i+l]
            if sub == sub[::-1] and re.match("^[A-Za-z]*$", sub):
                palindromes.add(sub.lower())
    return palindromes
