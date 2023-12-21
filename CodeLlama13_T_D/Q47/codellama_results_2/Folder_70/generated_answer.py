
def palindromes_of_specific_lengths(string):
    length = len(string)
    if 10 <= length <= 70:
        substr = string[10:70]
        return {pal for pal in substr.split() if len(pal) >= 24 and len(pal) <= 52 and pal == pal[::-1]}
    else:
        return set()
