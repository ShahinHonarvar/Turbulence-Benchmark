
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    for char in string[13:35]:
        if char in vowels and '8' < char <= 'F':
            valid_vowels.append(char)
    return valid_vowels
