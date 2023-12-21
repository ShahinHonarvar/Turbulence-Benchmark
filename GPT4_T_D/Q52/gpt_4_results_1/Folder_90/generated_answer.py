
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]

    s = ''.join(c for c in s.lower() if c.isalpha())
    return set(s[i:i+318] for i in range(len(s)-317) if is_palindrome(s[i:i+318]))
