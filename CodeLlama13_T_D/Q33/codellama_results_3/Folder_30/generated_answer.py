
def return_vowels(string):
    vowels = []
    for i in range(11, 61):
        if string[i].isalpha() and string[i].upper() in "AEIOUWY":
            vowels.append(string[i])
    return vowels
