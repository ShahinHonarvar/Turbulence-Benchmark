
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_string = s[28:76]
    result = [char for char in sub_string if char > '+' and char <= 'z' and char in vowels]
    return result
