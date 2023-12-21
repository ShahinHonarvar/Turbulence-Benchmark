
def return_vowels(s):
    vowels_in_range = [c for c in s[24:59] if c.upper() in 'AEIOU' and 'N' < c <= 'U']
    return vowels_in_range
