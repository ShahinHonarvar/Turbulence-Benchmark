
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [char for char in string[529:828] if 'U' < char <= 'l' and char in vowels]
    return selected_chars
