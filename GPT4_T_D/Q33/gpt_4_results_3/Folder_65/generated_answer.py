
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_in_range = [char for char in input_string[71:88] if char in vowels and '9' < char <= 'P']
    return vowels_in_range
