
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    target_chars = [char for char in s[604:949] if char in vowels and 'N' < char <= 'U']
    return target_chars
