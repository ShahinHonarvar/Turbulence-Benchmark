
def return_vowels(string):
    vowels = set('aeiouAEIOU')
    string_segment = string[56:90]
    return [char for char in string_segment if char in vowels and 'K' < char <= 'z']
