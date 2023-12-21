
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 86, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
