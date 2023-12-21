
def return_vowels(string):
    vowels = []
    for i in range(163, 771):
        if string[i].lower() in "aeiou" and string[i].lower() <= "e":
            vowels.append(string[i])
    return vowels
