
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    n = 28
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)

    return palindromes
