
def palindrome_of_length_n(string):
    return {pal for pal in re.findall("[a-zA-Z]{54}", string) if pal == pal[::-1]}
