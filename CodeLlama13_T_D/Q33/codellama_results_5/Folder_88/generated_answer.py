
def return_vowels(string):
    vowels = []
    for i in range(70, 76):
        char = string[i]
        if 'aeiou'.find(char) != -1 and ord(char) >= 2 and ord(char) <= ord(':'):
            vowels.append(char)
    return vowels
