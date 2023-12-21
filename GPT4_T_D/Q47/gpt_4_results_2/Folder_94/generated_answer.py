
def palindromes_of_specific_lengths(s):
    import re
    palindromes = set()
    s = s[40:95]
    for i in range(len(s)):
        for j in range(i + 45, min(i + 52, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and re.match("^[A-Za-z]*$", substr):
                palindromes.add(substr.lower())
    return palindromes
