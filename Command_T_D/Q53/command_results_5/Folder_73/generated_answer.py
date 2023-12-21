def palindrome_of_length_at_least_n(s):
    if len(s) < 2:
        return set()
    if s == s[::-1]:
        return {s}
    return {p for p in palindrome_of_length_at_least_n(s[1:]) if p[0] in s[::-1][1:-1]]
