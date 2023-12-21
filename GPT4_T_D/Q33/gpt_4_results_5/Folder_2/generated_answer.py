
def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[170:645] if char.lower() in vowels and 'E' < char <= '~']
    return result
