
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[43:70] if char in vowels and '*' < char <= 'b']
