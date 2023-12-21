
def return_vowels(string):
    vowels = []
    for i in range(11, 53):
        if string[i].isalpha() and string[i] in "AEIOU":
            vowels.append(string[i])
    return vowels
