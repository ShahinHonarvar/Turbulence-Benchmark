def palindrome_of_length_at_least_n(s):
    return {x for x in set(s.lower()) if len(x) > 48 and x[::-1] == x}
