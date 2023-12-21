def palindrome_of_length_at_least_n(s):
    s = set(s.lower())
    return set(s) & {s[i:i + 122] for i in range(0, len(s), 122)}
