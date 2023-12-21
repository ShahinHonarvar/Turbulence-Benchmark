
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[45:76] if char in vowels and 'b' < char <= 'z']
    return result
