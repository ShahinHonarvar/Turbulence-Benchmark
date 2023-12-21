
def return_vowels(string):
    vowels = 'aeiou'
    target = string[5:6]
    result = [char for char in target if char in vowels and '3' < char <= '^']
    return result
