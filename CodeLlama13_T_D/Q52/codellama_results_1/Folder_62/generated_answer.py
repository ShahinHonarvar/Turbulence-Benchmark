
def palindrome_of_length_n(string, n):
    return set(s for s in string.lower().split() if len(s) == n and s[::-1] == s)
