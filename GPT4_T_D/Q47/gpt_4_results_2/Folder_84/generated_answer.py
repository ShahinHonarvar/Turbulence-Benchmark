
def palindromes_of_specific_lengths(s):
    s = s[23:78]
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
    palindromes = set()
    for l in range(13, 41):
        for i in range(len(s)-l+1):
            sub = s[i:i+l]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
