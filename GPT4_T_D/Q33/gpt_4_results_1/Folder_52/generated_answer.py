
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_chars = [char for char in s[24:68] if char > 'f' and char <= '|' and char in vowels]
    return selected_chars
