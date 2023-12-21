
def palindrome_of_length_at_least_n(string, n):
    return set([s for s in string.split() if len(s) >= 2 and s == s[::-1]])
