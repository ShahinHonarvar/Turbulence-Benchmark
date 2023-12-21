
def palindrome_of_length_at_least_n(string, n):
    return {s[::-1] for s in string.split() if len(s) >= 70 and s == s[::-1]}
