
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [char for char in string[21:59] if '/' < char <= 'a' and char in vowels]
    return selected_chars
