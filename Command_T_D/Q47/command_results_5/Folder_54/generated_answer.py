def palindromes_of_specific_lengths(s):
    import re
    return set(re.findall(r'[a-z]+\d{3}([a-z]+){9}\d{3}[a-z]+', s[27:-1], flags=re.I))
