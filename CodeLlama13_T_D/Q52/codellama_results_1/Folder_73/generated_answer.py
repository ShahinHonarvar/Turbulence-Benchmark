
def palindrome_of_length_n(string):
    return {s for s in set(string) if s[::-1] == s and len(s) == 41}
