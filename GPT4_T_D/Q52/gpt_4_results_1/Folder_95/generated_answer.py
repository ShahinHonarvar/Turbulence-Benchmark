
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]

    s = ''.join(c for c in s if c.isalpha()).lower()
    results = set()
    for i in range(len(s) - 86):
        substr = s[i:i+87]
        if is_palindrome(substr):
            results.add(substr)
    return results
