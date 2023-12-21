def palindrome_of_length_at_least_n(s):
    return set(x for x in s.lower() if x[0] == x[-1] and len(x) > 80)
