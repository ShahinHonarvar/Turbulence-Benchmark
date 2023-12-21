
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o']
    relevant_string = string[273:275]
    found_vowels = [char for char in relevant_string if char in vowels and char > '+' and char <= 'o']
    return found_vowels
