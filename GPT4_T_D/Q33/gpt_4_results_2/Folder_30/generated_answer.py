
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_list = list(s[11:61])
    valid_chars = [char for char in s_list if char in vowels and 'M' < char <= 'W']
    return valid_chars
