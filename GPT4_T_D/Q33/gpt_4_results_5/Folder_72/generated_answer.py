
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in s[37:57] if char in vowels and char > '*' and char <= 'P']
