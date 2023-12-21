
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    valid_characters = [ch for ch in s[24:64] if 'F' < ch <= 'h']
    return [ch for ch in valid_characters if ch in vowels]
