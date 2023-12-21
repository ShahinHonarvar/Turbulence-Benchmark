
def return_vowels(string):
    vowels = []
    for char in string[86:99]:
        if 'AEIOUaeiou'.find(char) != -1 and char <= 'r':
            vowels.append(char)
    return vowels
