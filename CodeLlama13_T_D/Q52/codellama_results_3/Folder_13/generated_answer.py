
def palindrome_of_length_n(s):
    return set((c + c[::-1]) for c in s if len(c) == 206 and all(i.isalpha() for i in c))
