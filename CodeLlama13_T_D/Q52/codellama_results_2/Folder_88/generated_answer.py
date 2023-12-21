
def palindrome_of_length_n(string, n):
    return {s for s in {a+b for a in string for b in string} if len(s) == n and s == s[::-1]}
