
def return_vowels(string):
    vowels = []
    for i in range(60, 100):
        char = string[i]
        if 'aeiouAEIOU'.find(char) != -1 and char > 'j' and char <= 'n':
            vowels.append(char)
    return vowels
