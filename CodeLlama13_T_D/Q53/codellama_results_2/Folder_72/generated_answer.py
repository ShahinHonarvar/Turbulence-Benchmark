
def palindrome_of_length_at_least_n(string, n):
    return {s for s in string.split() if len(s) >= n and s == s[::-1]}
