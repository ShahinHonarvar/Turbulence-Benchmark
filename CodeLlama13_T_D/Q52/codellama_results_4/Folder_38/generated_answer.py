
def palindrome_of_length_n(s):
    return {pal for pal in set(s) if len(pal) == 38 and pal.lower() == pal[::-1]}
