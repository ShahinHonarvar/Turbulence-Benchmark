
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered = [char for char in s[56:96] if '&' < char <= 'T']
    return [char for char in filtered if char in vowels]
