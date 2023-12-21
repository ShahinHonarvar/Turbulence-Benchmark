
def return_vowels(str_value):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_vowels = [char for char in str_value[46:90] if char in vowels and '@' < char <= '[']
    return str_vowels
