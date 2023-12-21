
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_vowels = [char for char in string[8:9] if char in vowels and 'Y' < char <= 's']
    return selected_vowels
