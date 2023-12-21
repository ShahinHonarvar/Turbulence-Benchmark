
def palindrome_of_length_at_least_n(string, n):
    return {pal for pal in string if len(pal) >= n and pal == pal[::-1]}
