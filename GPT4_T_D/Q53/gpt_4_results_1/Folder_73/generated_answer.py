
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 94, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
