
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    slice_s = s[50:51]
    return [char for char in slice_s if char in vowels and char > ',' and char <= 'v']
