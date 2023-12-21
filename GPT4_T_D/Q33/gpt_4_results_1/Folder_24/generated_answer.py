
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string_vowels = [char for char in s[23:57] if char in vowels and '0' < char <= 'd']
    return string_vowels
