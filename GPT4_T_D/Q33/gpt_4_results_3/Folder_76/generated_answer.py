
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [c for c in s[495:837] if 'B' < c <= 't' and c in vowels]
    return selected_chars
