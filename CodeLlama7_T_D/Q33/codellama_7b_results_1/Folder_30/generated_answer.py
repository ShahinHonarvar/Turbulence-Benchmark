
def return_vowels(string):
    vowels = []
    for i in range(11, 62):
        if string[i].isalpha() and (string[i] > "M" or string[i] <= "W"):
            vowels.append(string[i])
    return vowels
