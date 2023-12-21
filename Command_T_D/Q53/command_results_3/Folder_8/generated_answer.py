def palindrome_of_length_at_least_n(s):
    return {p for p in (w.lower() for w in s.split()) if len(p) >= 45 and p == p[::-1]}
