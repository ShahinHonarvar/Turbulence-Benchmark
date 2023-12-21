
def return_vowels(string):
    vowels = []
    for char in string[23:85]:
        if 'a' <= char <= 'v':
            vowels.append(char)
    return vowels
