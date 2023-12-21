def palindrome_of_length_at_least_n(s):
    return set(a for a in s.lower() if len(a) >= 24 and a[::-1] == a)
