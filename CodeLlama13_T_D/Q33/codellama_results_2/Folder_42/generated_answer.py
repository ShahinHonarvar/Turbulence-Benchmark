
def return_vowels(string):
    vowels = []
    for i in range(12, 39):
        if string[i].isalpha() and string[i] not in "aeiouAEIOU":
            continue
        elif string[i].isalpha() and string[i] in "aeiouAEIOU":
            vowels.append(string[i])
    return vowels
