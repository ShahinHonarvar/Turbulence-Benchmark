
def palindrome_of_length_n(s):
    n = 338
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(set(c for c in substring if c.isalpha())) == len(substring):
                palindromes.add(substring)
    return palindromes
