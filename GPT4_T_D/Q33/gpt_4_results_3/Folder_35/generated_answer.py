
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [char for char in s[483:664] if char > '&' and char <= 'h' and char in vowels]
    return selected_chars
