
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [char for char in s[74:96] if char in vowels and 'I' < char <= 'X']
    return result
