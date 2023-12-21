
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())

    def is_palindrome(s):
        return s == s[::-1]

    palindromes = {s[i: j] for i in range(len(s)) for j in range(i + 89, len(s) + 1)}
    palindromes = {p for p in palindromes if is_palindrome(p)}

    return palindromes
