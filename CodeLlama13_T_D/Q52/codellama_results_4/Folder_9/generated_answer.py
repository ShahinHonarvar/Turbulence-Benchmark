
def palindrome_of_length_n(s):
    return {p for p in set(s) if len(p) == 72 and p[::-1] in s}
