
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in s[24:59] if char in vowels and 'N' < char <= 'U']
    return filtered_vowels
