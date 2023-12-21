
def palindrome_of_length_at_least_n(s):
    # Returns True if the string is a palindrome, False otherwise
    def is_palindrome(s):
        return s == s[::-1]

    # Converts the string to lowercase and removes all non-alphabet characters
    def clean_string(s):
        return ''.join(c for c in s.lower() if c.isalpha())

    s = clean_string(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 32, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])

    return palindromes
