
def return_vowels(string):
    vowels = 'aeiou'
    valid_chars = [char for char in string[51:77] if '4' < char <= '=']
    return [char for char in valid_chars if char in vowels]
