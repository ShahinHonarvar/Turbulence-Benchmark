
def palindrome_of_length_n(s):
    import re

    def is_palindrome(s):
        return s == s[::-1]

    s = ''.join(
        [char for char in s if char.isalpha()]
    ).lower()

    palindromes = set()

    for i in range(0, len(s)-46+1):
        substring = s[i:i+46]

        if is_palindrome(substring):
            palindromes.add(substring)

    return palindromes
