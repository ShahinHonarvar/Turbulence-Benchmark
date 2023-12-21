
def return_vowels(string):
    vowels = []
    for char in string[170:645]:
        if 'A' <= char <= '~':
            vowels.append(char)
    return vowels
