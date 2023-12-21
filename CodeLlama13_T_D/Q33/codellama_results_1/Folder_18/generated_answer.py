
def return_vowels(string):
    vowels = "aeiouAEIOU"
    return [char for char in string[528:606] if char > 'M' and char <= 'X' and char in vowels]
