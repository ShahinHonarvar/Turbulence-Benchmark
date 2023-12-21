
def palindrome_of_length_at_least_n(string):
    return {pal for pal in findall(r'[A-Za-z]{19,}', string) if pal == pal[::-1]}
