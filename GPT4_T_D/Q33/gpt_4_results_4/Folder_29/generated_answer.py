
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[19:20] if char in vowels and 'p' >= char > '<']
    return result
