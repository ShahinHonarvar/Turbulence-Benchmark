
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = string[70:76]
    selected_vowels = [char for char in selected_chars if char in vowels and '2' < char <= ':']
    return selected_vowels
