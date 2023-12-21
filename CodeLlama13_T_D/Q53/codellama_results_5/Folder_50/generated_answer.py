
def palindrome_of_length_at_least_n(string):
    return {pal for pal in set(string) if len(pal) >= 91 and pal == pal[::-1]}
