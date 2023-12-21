
def return_vowels(string):
    vowels = []
    for i in range(34, 69):
        if string[i].isalpha() and string[i] > "_" and string[i] <= "o":
            vowels.append(string[i])
    return vowels
