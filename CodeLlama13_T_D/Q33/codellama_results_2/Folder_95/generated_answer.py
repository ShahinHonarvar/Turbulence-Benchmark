
def return_vowels(string):
    vowels = []
    for char in string[32:61]:
        if 'AEIOUaeiou'.find(char) != -1 and char <= 'P':
            vowels.append(char)
    return vowels
