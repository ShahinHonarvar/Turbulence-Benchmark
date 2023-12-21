
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[21:59] if char > '/' and char <= 'a' and char in vowels]
