
def palindrome_of_length_n(s):
    s = ''.join(c for c in s if c.isalpha())
    s = s.lower()
    n = 95
    palindromes = set()
    for i in range(len(s)-n+1):
        substr = s[i:i+n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
