
def return_vowels(s):
    chars = s[29:73]
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    return [char for char in chars if char > '#' and char <= '(' and char in vowels]
