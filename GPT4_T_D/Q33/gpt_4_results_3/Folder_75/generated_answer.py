
def return_vowels(string):
    vowels = 'AEIOU'
    substring = string[20:41]
    return [c for c in substring if c in vowels and 'K' < c <= 'Z']   
