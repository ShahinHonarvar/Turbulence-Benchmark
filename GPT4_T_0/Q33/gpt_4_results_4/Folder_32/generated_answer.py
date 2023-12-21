
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in s[45:76] if char in vowels and 'b' < char <= 'z']
