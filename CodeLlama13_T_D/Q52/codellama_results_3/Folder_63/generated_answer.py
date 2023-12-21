
def palindrome_of_length_n(s):
    return {p for p in substrings_of_length_18(s) if is_palindrome(p)}

def substrings_of_length_18(s):
    return [s[i:i+18] for i in range(len(s)-17)]

def is_palindrome(s):
    return s == s[::-1] and all(c.isalpha() for c in s)
