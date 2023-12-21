
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    substrings = set(s[i:i+74] for i in range(len(s)))
    palindromes = set(sub for sub in substrings if sub == sub[::-1])
    return palindromes
