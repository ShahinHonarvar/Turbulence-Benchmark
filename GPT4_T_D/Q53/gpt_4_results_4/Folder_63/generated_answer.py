
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + 37 - 1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                palindromes.add(s[i:j+1])

    return palindromes
