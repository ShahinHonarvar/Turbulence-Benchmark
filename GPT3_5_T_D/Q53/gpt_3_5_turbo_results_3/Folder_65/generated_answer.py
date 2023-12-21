
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 15, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= 15 and substr == substr[::-1] and all(c in string.ascii_letters for c in substr):
                palindromes.add(substr)
    return palindromes
