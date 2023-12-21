
def palindrome_of_length_n(s):
    return {pal for pal in re.findall('[A-Za-z]{20}', s) if pal == pal[::-1]}
