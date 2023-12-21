
def palindrome_of_length_at_least_n(string):
    return {s for s in string.split() if s == s[::-1]}
