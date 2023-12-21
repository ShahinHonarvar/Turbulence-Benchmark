
def return_vowels(string):
    vowels = []
    for i in range(74, 96):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "I":
            vowels.append(string[i])
    return vowels
