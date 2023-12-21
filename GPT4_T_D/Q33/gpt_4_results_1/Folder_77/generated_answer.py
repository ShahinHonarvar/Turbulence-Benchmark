
def return_vowels(string_arg):
    substring = string_arg[837:975]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [ch for ch in substring if ch in vowels and 'N' < ch <= 'W']
