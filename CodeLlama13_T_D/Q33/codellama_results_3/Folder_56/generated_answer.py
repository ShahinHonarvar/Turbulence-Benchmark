
def return_vowels(string):
    vowels = []
    for i in range(15, 86):
        if string[i].isalpha() and string[i] not in "AEIOUaeiou":
            vowels.append(string[i])
    return vowels
