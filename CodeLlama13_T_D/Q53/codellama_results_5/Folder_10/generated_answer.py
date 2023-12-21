
def palindrome_of_length_at_least_n(string):
    return {pal for pal in re.findall(r'[A-Za-z]{92,}', string) if pal == pal[::-1]}
