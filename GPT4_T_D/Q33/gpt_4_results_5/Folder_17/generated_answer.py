
def return_vowels(string):
    vowels = 'aeiou'
    sub_string = string[60:99]
    return [char for char in sub_string if char in vowels and 'j' < char <= 'n']
