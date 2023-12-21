
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[19:20] if char in vowels and 'p' >= char > '<']
    return result
