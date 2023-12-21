
def return_vowels(string):
    vowels = []
    for char in string[32:61]:
        if 'a' <= char <= 'p':
            vowels.append(char)
    return vowels
