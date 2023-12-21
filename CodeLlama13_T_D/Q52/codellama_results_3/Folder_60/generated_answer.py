
def palindrome_of_length_n(s):
    return set((x for x in (y for y in s if len(y) == 88) if y[::-1] == y))
