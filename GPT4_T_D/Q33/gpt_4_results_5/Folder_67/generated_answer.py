
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[21:59] if char in vowels and '/' < char <= 'a']
    return result
