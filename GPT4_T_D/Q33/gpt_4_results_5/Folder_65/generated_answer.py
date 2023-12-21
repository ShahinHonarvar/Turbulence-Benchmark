
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_chars = [char for char in string[71:88] if '9' < char <= 'P']
    return [char for char in selected_chars if char in vowels]
