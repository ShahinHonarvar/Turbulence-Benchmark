
def return_vowels(string):
    vowels = []
    for i in range(36, 56):
        if string[i].isalpha() and string[i].lower() in "aeiou" and ord(string[i]) > 97:
            vowels.append(string[i])
    return vowels
