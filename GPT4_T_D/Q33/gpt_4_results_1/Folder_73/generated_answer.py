
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sliced = s[47:89]
    result = [char for char in sliced if char in vowels and '@' < char <= 'n']
    return result
