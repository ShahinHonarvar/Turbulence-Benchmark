
def return_vowels(string):
    vowels = 'aeiou'
    sub_string = string[15:86]
    vowel_list = [char for char in sub_string if char in vowels and '@' < char <= '~' ]
    return vowel_list
