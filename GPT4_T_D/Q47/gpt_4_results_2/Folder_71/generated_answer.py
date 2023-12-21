
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:66].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+23, min(i+37, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1] and re.match("^[a-z]*$", substr):
                palindromes.add(substr)
    return palindromes
