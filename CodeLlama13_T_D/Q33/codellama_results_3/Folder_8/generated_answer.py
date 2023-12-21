
def return_vowels(string):
    vowels = []
    for char in string[64:82]:
        if 'aeiouAEIOU'.find(char) >= 0 and char < 'z':
            vowels.append(char)
    return vowels
