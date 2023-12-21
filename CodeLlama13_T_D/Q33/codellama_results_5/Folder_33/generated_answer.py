
def return_vowels(string):
    vowels = []
    for i in range(163, 771):
        if string[i].isalpha() and string[i] in "AEIOUaeiou" and string[i] not in vowels:
            vowels.append(string[i])
    return vowels
