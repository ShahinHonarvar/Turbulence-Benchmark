
def palindrome_of_length_at_least_n(s):
    return {pal for pal in s if len(pal) >= 64 and pal == pal[::-1]}
