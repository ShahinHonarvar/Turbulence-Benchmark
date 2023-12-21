
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in input_string[3:8] if char in vowels and ';' < char <= 'D']
    return filtered_vowels
