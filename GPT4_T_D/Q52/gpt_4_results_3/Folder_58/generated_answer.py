
def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    s = ''.join(c for c in s if c.isalpha())
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+223, len(s)+1):
            substr = s[i:j]
            if len(substr) == 223 and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes
