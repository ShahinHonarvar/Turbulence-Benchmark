
def palindrome_of_length_n(s):
    return {pal for pal in set(s) if pal == pal[::-1]}
