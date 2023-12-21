
def palindrome_of_length_n(string, n):
    return {s[::-1].lower() for s in string.split() if len(s) == n and s.isalpha()}
