
def palindrome_of_length_n(string, n):
    return set(s for s in (string * 2).split() if len(s) == n and s == s[::-1])
