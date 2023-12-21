
def palindromes_of_specific_lengths(s):
    import string
    s = s.lower()
    s = s[24:85]
    s = ''.join(ch for ch in s if ch in string.ascii_lowercase)
    palindromes = set()
    for length in range(21, 32):
        for start in range(len(s) - length + 1):
            subset = s[start:start+length]
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
