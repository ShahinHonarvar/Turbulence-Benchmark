
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    indices_range = string[170:645]
    char_range = [char for char in indices_range if char > 'E' and char <= '~']
    result = [vowel for vowel in char_range if vowel in vowels]
    return result
