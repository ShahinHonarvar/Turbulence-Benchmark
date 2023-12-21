
def return_vowels(input_string):
    vowels = "AEIOUaeiou"
    characters = input_string[71:88]
    result = [char for char in characters if char > '9' and char <= 'P' and char in vowels]
    return result
