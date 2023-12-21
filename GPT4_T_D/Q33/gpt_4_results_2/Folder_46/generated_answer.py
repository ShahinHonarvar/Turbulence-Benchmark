
def return_vowels(s):
    vowels = 'aeiou'
    output = [char for char in s[10:83] if char > '%' and char <= 'e' and char in vowels]
    return output
