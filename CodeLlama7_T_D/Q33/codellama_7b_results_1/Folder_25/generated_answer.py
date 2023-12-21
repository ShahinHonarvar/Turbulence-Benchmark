
def return_vowels(string):
    vowels = []
    for i in range(28, 76):
        if string[i].isalpha() and string[i].islower():
            if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
                vowels.append(string[i])
    return vowels
