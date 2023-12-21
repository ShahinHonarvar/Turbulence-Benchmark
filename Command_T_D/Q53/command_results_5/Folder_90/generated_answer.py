def palindrome_of_length_at_least_n(s):
    return set(filter(lambda s: s.lower() == s[::-1].lower(), s))
