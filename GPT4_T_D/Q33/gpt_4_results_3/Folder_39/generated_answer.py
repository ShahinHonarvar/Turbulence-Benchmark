
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[32:97] if char > 'Q' and char <= ']' and char in vowels]
    return result
