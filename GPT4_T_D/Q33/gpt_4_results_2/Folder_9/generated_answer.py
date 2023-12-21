
def return_vowels(string):
    vowels = 'aeiou'
    chars = list(string[13:35])
    return [char for char in chars if char in vowels and '8' < char <= 'F']
