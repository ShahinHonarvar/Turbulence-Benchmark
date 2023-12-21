
def return_vowels(string):
    vowels = []
    for i in range(1, 7):
        if string[i] > 'F' and string[i] <= 'j':
            if string[i] in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(string[i])
    return vowels
