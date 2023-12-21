
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s[55:65]
    result = [char for char in s if char in vowels and 'Z' < char <= 'w']
    return result
