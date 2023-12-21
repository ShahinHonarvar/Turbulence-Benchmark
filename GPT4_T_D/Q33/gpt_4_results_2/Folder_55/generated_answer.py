
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_chars = [char for char in s[1:5] if char > '!' and char <= 'j']
    return [char for char in selected_chars if char in vowels]
