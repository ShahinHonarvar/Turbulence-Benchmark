
def return_vowels(string):
    vowels = []
    for i in range(23, 75):
        if string[i].isalpha() and string[i].lower() in ["a", "e", "i", "o", "u"]:
            if string[i] > "L" and string[i] <= "d":
                vowels.append(string[i])
    return vowels
