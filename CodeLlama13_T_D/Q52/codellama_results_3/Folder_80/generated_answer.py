
def palindrome_of_length_n(string):
    return set((s[::-1]) for s in string.split() if len(s) == 276 and s == s[::-1])
