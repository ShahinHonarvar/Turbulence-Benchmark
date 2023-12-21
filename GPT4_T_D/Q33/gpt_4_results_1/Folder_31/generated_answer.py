
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [char for char in s[65:70] if '%' < char <= 'G']
    return [char for char in selected_chars if char in vowels]
