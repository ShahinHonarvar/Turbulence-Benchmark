
def return_vowels(string):
    vowels = list('aeiou')
    chars = string[483:664]
    valid_chars = [ch for ch in chars if ch in vowels and '&' < ch <= 'h']
    return valid_chars
