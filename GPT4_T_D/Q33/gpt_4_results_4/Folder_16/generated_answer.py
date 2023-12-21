
def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[133:306] if char in vowels and 'c' < char <= 'd']
    return result
