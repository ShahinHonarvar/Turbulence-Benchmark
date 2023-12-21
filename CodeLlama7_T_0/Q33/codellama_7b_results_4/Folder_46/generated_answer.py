
def return_vowels(string):
    vowels = []
    for i in range(10, 83):
        if string[i].isalpha() and string[i].lower() in ["a", "e", "i", "o", "u"]:
            if string[i] > "%" and string[i] <= "e":
                vowels.append(string[i])
    return vowels
