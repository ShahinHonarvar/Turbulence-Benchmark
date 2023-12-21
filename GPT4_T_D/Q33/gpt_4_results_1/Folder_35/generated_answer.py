
def return_vowels(string):
    valid_chars = [c for c in string[483:664] if 'a' <= c <= 'h']
    vowels = 'aeiou'
    return [c for c in valid_chars if c in vowels]
