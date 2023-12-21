
def palindrome_of_length_at_least_n(s):
    import string
    allowed_chars = set(string.ascii_letters)
    s = ''.join(c for c in s if c in allowed_chars).lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+86, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])

    return palindromes
