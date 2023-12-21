
def return_vowels(string):
    vowels = 'aeiou'
    char_range = string[56:96]
    result = [char for char in char_range
              if char in vowels and 'T' >= char > '&']
    return result
