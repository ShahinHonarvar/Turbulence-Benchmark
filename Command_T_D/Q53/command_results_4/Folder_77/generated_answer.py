def palindrome_of_length_at_least_n(s):
    return set(p for p in s.lower() if len(p) >= 149 and p == p[::-1])
