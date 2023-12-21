
def return_vowels(string):
    vowels = []
    for char in string[641:872]:
        if 'a' <= char <= 'q':
            vowels.append(char)
    return vowels
