
def return_vowels(input_string):
    vowels = "aeiouAEIOU"
    return [char for char in input_string[20:41] if char in vowels and 'K' < char <= 'Z']
