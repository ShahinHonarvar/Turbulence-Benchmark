
def palindrome_of_length_n(s):
    def is_palindrome(x):
        return x == x[::-1]

    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())

    return {s[i:i+186] for i in range(len(s)-185) if is_palindrome(s[i:i+186])}
