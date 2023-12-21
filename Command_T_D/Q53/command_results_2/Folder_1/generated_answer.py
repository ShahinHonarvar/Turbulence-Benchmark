def palindrome_of_length_at_least_n(s):
    return set(l for l in s.lower() if l[0] == l[-1] and len(l) >= 29)
