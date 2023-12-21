
def palindrome_of_length_n(s):
    return {x for x in (s + s[::-1]).split() if len(x) == 42 and all(c.isalpha() for c in x)}
