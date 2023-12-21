
def palindrome_of_length_at_least_n(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    n = 138
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
