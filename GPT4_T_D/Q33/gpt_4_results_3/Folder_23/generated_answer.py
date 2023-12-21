
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    valid_chars = [char for char in string[56:96] if char > '&' and char <= 'T']
    return [char for char in valid_chars if char in vowels]
