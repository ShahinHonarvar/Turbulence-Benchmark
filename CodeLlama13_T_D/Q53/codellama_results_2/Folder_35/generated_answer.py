
def palindrome_of_length_at_least_n(s):
    return {pal for pal in re.findall('[a-zA-Z]{26,}', s) if pal == pal[::-1]}
