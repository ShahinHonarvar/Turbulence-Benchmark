
def return_vowels(string):
    vowels = []
    for char in string:
        if ord(char) >= 64 and ord(char) <= 82 and char > 'P' and char <= 'z':
            vowels.append(char)
    return vowels
