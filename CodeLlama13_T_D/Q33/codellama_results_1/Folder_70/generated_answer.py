
def return_vowels(string):
    vowels = []
    for char in string[170:403]:
        if 'aeiouAEIOU'.find(char) != -1 and ord(char) > 73 and ord(char) <= 75:
            vowels.append(char)
    return vowels
