
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[19:32] if char >= '0' and char <= '7' and char in vowels]
