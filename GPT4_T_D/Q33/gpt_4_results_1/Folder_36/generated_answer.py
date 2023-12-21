
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    selected_vowels = [char for char in s[604:949] if char in vowels and 'N' < char <= 'U']
    return selected_vowels
