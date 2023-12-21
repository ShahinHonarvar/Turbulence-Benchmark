
def return_vowels(string):
    vowels = []
    for i in range(10, 97):
        char = string[i]
        if char >= 'R' and char <= 'b':
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(char)
    return vowels
