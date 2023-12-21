
def return_vowels(string):
    vowels = []
    for i in range(21, 24):
        if string[i].isalpha() and string[i] not in "aeiouAEIOU":
            continue
        vowels.append(string[i])
    return vowels
