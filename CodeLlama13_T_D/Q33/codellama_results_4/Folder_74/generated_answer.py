
def return_vowels(string):
    vowels = []
    for char in string[69:82]:
        if char >= '[' and char <= '~':
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(char)
    return vowels
