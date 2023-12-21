
def return_vowels(str):
    str = str[23:57]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in str if char in vowels and '0' < char <= 'd']
