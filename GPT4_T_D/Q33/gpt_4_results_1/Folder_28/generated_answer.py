
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    allowed_chars = [char for char in string[41:50] if 'W' < char <= '[']
    return [char for char in allowed_chars if char in vowels]
