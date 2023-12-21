
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s.lower() if c.isalpha())
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 18, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
