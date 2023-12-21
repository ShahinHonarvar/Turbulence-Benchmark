
def return_vowels(string):
    vowels = []
    for char in string[260:322]:
        if 'a' <= char <= 'u':
            vowels.append(char)
    return vowels
