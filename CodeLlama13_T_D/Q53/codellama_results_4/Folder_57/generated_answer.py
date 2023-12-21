
def palindrome_of_length_at_least_n(s):
    return {pal for pal in set(s) if len(pal) >= 93 and pal == pal[::-1]}
