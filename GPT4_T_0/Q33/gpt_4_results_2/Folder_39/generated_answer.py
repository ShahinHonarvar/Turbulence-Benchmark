
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in s[32:97] if char in vowels and 'Q' < char <= ']']
