
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    slice_s = s[8:9]
    return [char for char in slice_s if char in vowels and 'Y' < char <= 's']
