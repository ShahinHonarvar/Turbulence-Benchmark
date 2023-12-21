
def return_vowels(s):
    vowels = 'aeiou'
    list_chars = [char for char in s[19:20] if char in vowels and 'p' >= char > '<']
    return list_chars
