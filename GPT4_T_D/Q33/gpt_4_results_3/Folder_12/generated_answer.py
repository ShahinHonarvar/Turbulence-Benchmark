
def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[13:37] if char.lower() in vowels and 'Z' < char <= '}']
    return result
