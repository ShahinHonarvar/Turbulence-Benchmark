
def palindrome_of_length_at_least_n(string):
    return set([pal for pal in re.findall('[A-Za-z]{10,}', string) if pal == pal[::-1]])
