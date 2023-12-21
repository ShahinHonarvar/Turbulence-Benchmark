
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    vowels_in_range = [c for c in s[529:828] if c in vowels and 'U' < c <= 'l']
    return vowels_in_range
