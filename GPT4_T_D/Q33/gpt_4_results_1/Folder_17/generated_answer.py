
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    returned_vowels = [char for char in s[60:99] if char in vowels and 'j' < char <= 'n']
    return returned_vowels
