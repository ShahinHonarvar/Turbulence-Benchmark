
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if len(s) > 97:
        valid_chars = [char for char in s[10:97] if char in vowels and 'R' < char <= 'b']
        return valid_chars
    else:
        return []
