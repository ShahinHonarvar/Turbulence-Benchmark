
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_characters = input_string[23:57]
    valid_characters = [char for char in selected_characters if char > '0' and char <= 'd' and char in vowels]
    return valid_characters
