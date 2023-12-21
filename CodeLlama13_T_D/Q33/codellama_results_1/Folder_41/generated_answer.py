
def return_vowels(string):
    vowels = []
    for i in range(71, 81):
        if string[i].lower() in ["a", "e", "i", "o", "u"]:
            vowels.append(string[i])
    return vowels
