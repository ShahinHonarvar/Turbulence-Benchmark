
def palindrome_of_length_at_least_n(string):
    return {pal for pal in re.findall(r'[a-zA-Z]{147,}', string) if pal == pal[::-1]}
