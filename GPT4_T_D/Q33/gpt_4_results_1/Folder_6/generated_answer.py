
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in string[20:34] if char in vowels and 'U' < char <= 'i']
    return result
