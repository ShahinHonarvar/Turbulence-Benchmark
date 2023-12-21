
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]

    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        if i + 84 <= len(s):
            substring = s[i:i+84]
            if is_palindrome(substring) and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
