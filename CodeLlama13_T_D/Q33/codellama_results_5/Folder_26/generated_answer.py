
def return_vowels(string):
    vowels = []
    for i in range(10, 82):
        char = string[i]
        if ord(char) > ord('$') and ord(char) <= ord('@'):
            vowels.append(char)
    return vowels
