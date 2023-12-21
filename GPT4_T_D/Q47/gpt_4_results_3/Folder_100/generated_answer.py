
def palindromes_of_specific_lengths(s):
    s = s[29:97]
    s = ''.join(c for c in s if c.isalpha())
    s = s.lower()
    pal_set = set()
    for i in range(len(s)):
        for j in range(12, 19):
            if i + j <= len(s):
                substring = s[i:i+j]
                if substring == substring[::-1]:
                    pal_set.add(substring)
    return pal_set
