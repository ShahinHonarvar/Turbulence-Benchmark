
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[1:5] if char in vowels and '!' < char <= 'j']
