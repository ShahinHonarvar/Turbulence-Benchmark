
def palindrome_of_length_n(s):
    return set((c * 2 for c in s if c.isalpha() and len(c) == n))
