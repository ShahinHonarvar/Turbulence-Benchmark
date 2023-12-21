
def return_vowels(text):
    vowels = 'aeiou'
    chars = text[77:84]
    result = [char for char in chars if char in vowels and 'G' >= char > '(']
    return result
