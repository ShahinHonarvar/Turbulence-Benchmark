def palindrome_of_length_at_least_n(s):
    return set(filter(lambda x: len(x) >= 28 and all(c.islower() for c in x), s))
