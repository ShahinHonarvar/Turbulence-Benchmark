
def return_vowels(s):
    vowels = 'aeiou'
    vowel_list = [char for char in s[40:91] if char in vowels and 'A' < char <= 'x']
    return vowel_list
