
def return_vowels(string):
    vowels = []
    for i in range(71, 82):
        if string[i].isalpha() and string[i].lower() in ["a", "e", "i", "o", "u"]:
            vowels.append(string[i])
    return vowels
