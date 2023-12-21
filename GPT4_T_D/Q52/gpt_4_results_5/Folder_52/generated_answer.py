
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s) - 422):
        substr = s[i:i+423]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes
