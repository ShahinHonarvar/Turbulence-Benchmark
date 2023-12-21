
def return_vowels(string):
    vowels = []
    for char in string[3:8]:
        if 'AEIOU'.find(char) != -1 and ord(char) <= ord('D'):
            vowels.append(char)
    return vowels
