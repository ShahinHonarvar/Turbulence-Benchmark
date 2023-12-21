
def return_vowels(string):
    vowels = []
    for i in range(85, 100):
        if string[i].isalpha() and string[i] in "aeiouAEIOU" and string[i] > "/" and string[i] <= "n":
            vowels.append(string[i])
    return vowels
