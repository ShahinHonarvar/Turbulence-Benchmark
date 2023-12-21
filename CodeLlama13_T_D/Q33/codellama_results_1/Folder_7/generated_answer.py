
def return_vowels(string):
    vowels = []
    for char in string[202:872]:
        if 'AEIOU'.find(char) != -1 and ord(char) > 3:
            vowels.append(char)
    return vowels
