
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    for char in s[1:5]:
        if char > '!' and char <= 'j' and char in vowels:
            valid_vowels.append(char)
    return valid_vowels
