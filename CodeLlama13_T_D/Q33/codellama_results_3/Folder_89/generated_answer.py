
def return_vowels(string):
    vowels = []
    for i in range(50, 51):
        if string[i].isalpha() and string[i] in "aeiouAEIOU":
            vowels.append(string[i])
    return vowels
