
def palindrome_of_length_at_least_n(string):
    return {s for s in set(string.split()) if len(s) >= 47 and s == s[::-1]}
