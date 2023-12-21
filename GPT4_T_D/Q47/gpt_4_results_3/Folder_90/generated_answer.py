
def palindromes_of_specific_lengths(s):
    import re
    s = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if re.search('^[A-Za-z]*$', substring) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes
