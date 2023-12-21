def palindrome_of_length_at_least_n(s):
    return set(a[::-1] for a in s.lower() if len(a) > 89)
