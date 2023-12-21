
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_output = [char for char in s[11:61] if char in vowels and 'M' < char <= 'W']
    return vowel_output
