def palindromes_of_specific_lengths(s):
    return set(a for a in s[27:-1] if a[0].isalpha() and len(a) in (18, 19))
