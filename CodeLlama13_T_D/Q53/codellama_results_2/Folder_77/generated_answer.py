
def palindrome_of_length_at_least_n(string):
    return {s for s in string.split() if s[::-1] == s and len(s) >= 149}
