
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    selected_chars = [char for char in string[8:9] if (char > 'Y' and char <= 's') and char in vowels]
    return selected_chars
