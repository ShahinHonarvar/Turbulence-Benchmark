
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = s[328:455]
    return [char for char in substring if char in vowels and '>' < char <= 'z']
