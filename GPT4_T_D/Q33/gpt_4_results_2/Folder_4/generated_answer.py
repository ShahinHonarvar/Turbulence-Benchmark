
def return_vowels(s):
    vowels = 'aeiou'
    s_slices = s[40:91]
    return [ch for ch in s_slices if ch.lower() in vowels and 'A' < ch <= 'x']
