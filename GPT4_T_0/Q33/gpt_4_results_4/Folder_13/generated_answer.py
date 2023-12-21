
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in s[149:313] if char in vowels and 'M' < char <= 'j']
    return result
