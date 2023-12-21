
def palindrome_of_length_at_least_n(string):
    return {pal for pal in re.findall('[a-zA-Z]{64,}', string) if pal == pal[::-1]}
