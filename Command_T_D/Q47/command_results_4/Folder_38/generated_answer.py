def palindromes_of_specific_lengths(str):
    str = str[18:87].lower()
    return {i[::-1] for i in str[38:-2][::2][1:-1] if all(c.isalpha() for c in i)}
