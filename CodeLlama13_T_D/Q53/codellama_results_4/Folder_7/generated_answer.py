
def palindrome_of_length_at_least_n(string):
    return {pal for pal in set(re.findall("[a-zA-Z]{12,}", string)) if pal == pal[::-1]}
