
def return_vowels(s):
    vowels = []
    for letter in s[54:82]:
        if letter >= '=' and letter <= '@':
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(letter)
    return vowels
