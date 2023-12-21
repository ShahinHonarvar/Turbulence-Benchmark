
def return_vowels(string):
    vowels = []
    for i in range(19, 32):
        if string[i].isalpha() and string[i] in "AEIOUaeiou":
            vowels.append(string[i])
    return vowels
