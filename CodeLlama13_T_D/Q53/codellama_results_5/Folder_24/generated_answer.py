
def palindrome_of_length_at_least_n(string):
    return {pal for pal in re.findall('[A-Za-z]{53,}', string) if pal == pal[::-1]}
