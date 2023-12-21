
def return_vowels(string):
    vowels = []
    for i in range(60, 99):
        if string[i].islower() and string[i] in "aeiou":
            vowels.append(string[i])
    return vowels
