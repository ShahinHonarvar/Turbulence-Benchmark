
def return_vowels(s):
    vowels = 'aeiou'
    result = [letter for letter in s[641:872] if letter in vowels and 'a' <= letter <= 'q']
    return result
