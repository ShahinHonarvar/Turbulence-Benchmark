
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 173, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
