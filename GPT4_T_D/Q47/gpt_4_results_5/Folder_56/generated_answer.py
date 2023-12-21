
def palindromes_of_specific_lengths(s):
    import re
    s = s[1:10].lower()
    palindromes = set()
    for i in range(3, 8):
        for j in range(len(s)):
            substr = s[j:j + i]
            if substr == substr[::-1] and re.match("^[a-z]*$", substr):
                palindromes.add(substr)
    return palindromes
