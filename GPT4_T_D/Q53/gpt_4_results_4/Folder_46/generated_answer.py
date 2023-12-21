
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 86, len(s) + 1):
            substr = s[start:end]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
