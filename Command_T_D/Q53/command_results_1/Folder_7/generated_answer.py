def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return {s[:i] + s[::-1][i:] for i in range(1, len(s) + 1)}
