
def return_vowels(string):
    vowels = []
    for i in range(170, 645):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "e":
            vowels.append(string[i])
    return vowels
