
def return_vowels(string):
    vowels = []
    for char in string:
        if ord('A') <= ord(char) <= ord('G'):
            if char in 'AEIOU':
                vowels.append(char)
    return vowels
