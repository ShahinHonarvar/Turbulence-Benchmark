
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)-2):
        substr = ''.join([c for c in s[i:i+3] if c.isalpha()])
        if len(substr) == 3 and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
