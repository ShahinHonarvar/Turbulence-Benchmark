
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+67, len(s)+1):
            substr = s[i:j]
            if all(c.isalpha() for c in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
