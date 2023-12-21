
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[77:84] if char in vowels and '(' < char <= 'G']
    return result
