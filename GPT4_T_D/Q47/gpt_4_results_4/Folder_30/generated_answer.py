
def palindromes_of_specific_lengths(s):
    import re
    s = s[14:91]
    s = re.sub("[^A-Za-z]", "", s)
    s = s.lower()
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(s)):
            substr = s[i:i+length]
            if substr == substr[::-1] and len(substr) == length:
                palindromes.add(substr)
    return palindromes
