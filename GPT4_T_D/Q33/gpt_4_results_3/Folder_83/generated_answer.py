
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']   
    return [char for char in s[90:97] if char > '_' and char <= 'x' and char in vowels]
