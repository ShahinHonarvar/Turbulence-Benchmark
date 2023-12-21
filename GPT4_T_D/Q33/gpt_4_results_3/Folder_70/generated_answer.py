
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    extract = input_string[171:402]
    return [char for char in extract if char in vowels and 'I' < char <= 'k']
