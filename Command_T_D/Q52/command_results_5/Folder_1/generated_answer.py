def palindrome_of_length_n(s):
    return set(c for c in s.lower() if c == c[::-1])
