
def palindromes_of_specific_lengths(s):
    s = ''.join(c for c in s if c.isalpha())
    s = s.lower()
    s = s[125:284]
    palindromes = set()
    for l in range(109, 127):
        for i in range(len(s) - l + 1):
            substring = s[i:i+l]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
