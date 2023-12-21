
def palindromes_of_specific_lengths(string):
    lengths = range(37, 61)
    substr = string[11:84]
    return {pal for pal in substr if len(pal) in lengths and pal == pal[::-1]}
