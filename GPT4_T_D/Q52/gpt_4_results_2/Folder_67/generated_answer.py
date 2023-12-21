
def palindrome_of_length_n(s):
    s = s.lower()
    n = 42
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and all(c.isalpha() for c in substr):
                palindromes.add(substr)
    return palindromes
