
def palindrome_of_length_at_least_n(s):
    return {pal for pal in re.findall(r'[a-zA-Z]{83,}', s) if pal == pal[::-1]}
