def palindrome_of_length_at_least_n(s):
    return set(x for x in s.lower() if x == x[::-1])
