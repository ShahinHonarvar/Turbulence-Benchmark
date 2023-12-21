
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    target_characters = [char for char in s[43:70] if char > '*' and char <= 'b']
    return [char for char in target_characters if char in vowels]
