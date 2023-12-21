
def palindrome_of_length_at_least_n(string):
    return {pal for pal in string if len(pal) >= 32 and pal == pal[::-1]}
