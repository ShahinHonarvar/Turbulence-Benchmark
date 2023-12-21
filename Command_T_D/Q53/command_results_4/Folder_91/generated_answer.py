def palindrome_of_length_at_least_n(s):
    return {x for x in set(s.lower()) if len(x) > 6 and x == x[::-1] }
