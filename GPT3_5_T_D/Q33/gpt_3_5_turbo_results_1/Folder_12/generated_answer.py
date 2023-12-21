
def return_vowels(string):
    vowels = []
    for char in string[13:37]:
        if 'Z' < char <= '}':
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(char)
    return vowels
