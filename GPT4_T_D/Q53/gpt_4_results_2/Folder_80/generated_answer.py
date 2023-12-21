
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    n = 30
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
