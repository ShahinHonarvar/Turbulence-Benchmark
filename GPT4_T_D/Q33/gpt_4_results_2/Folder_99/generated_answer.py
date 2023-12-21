
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    char_range = [char for char in s[323:526] if '+' < char <= ':']
    vowel_list = [char for char in char_range if char in vowels]
    return vowel_list
