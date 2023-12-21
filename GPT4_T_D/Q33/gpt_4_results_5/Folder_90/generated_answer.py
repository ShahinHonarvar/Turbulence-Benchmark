
def return_vowels(s):
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = s[142:145]
    character_compared = [chr for chr in s if chr > '4' and chr <= 'o' and chr in vowel_set]
    return character_compared
